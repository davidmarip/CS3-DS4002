"""
Helper Functions for Airline Delay Analysis
============================================

This module provides utility functions to assist students with the 
airline delay scorecard case study.

Author: David Marip, UVA DS4002
Date: December 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_validate_data(filepath):
    """
    Load the airline delay dataset and perform basic validation checks.
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file containing airline delay data
        
    Returns:
    --------
    pd.DataFrame
        Loaded dataset
        
    Raises:
    -------
    FileNotFoundError
        If the file doesn't exist
    ValueError
        If required columns are missing
    """
    # Load data
    df = pd.read_csv(filepath)
    
    # Check for required columns
    required_cols = ['CarrierName', 'ArrDelay15', 'Cancelled', 'ArrDelayMinutes']
    missing_cols = [col for col in required_cols if col not in df.columns]
    
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    print(f"✅ Data loaded successfully!")
    print(f"   Total records: {len(df):,}")
    print(f"   Date range: {df['Year'].min()}-{df['Year'].max()}")
    print(f"   Airlines: {df['CarrierName'].nunique()}")
    
    return df


def compute_delay_rate(df, group_by='CarrierName', exclude_cancelled=True):
    """
    Compute delay rate (% of flights with ArrDelay15 = 1) by group.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with flight records
    group_by : str or list
        Column(s) to group by (default: 'CarrierName')
    exclude_cancelled : bool
        If True, exclude cancelled flights (default: True)
        
    Returns:
    --------
    pd.DataFrame
        Aggregated metrics with delay rate by group
    """
    # Filter out cancelled flights if requested
    if exclude_cancelled:
        df = df[df['Cancelled'] == 0].copy()
    
    # Compute metrics
    metrics = df.groupby(group_by).agg(
        total_flights=('ArrDelay15', 'count'),
        delayed_flights=('ArrDelay15', 'sum')
    ).reset_index()
    
    # Calculate delay rate percentage
    metrics['delay_rate_pct'] = (
        metrics['delayed_flights'] / metrics['total_flights'] * 100
    )
    
    # Sort by worst performers
    metrics = metrics.sort_values('delay_rate_pct', ascending=False)
    
    return metrics


def compute_cancellation_rate(df, group_by='CarrierName'):
    """
    Compute cancellation rate by group.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with flight records
    group_by : str or list
        Column(s) to group by (default: 'CarrierName')
        
    Returns:
    --------
    pd.DataFrame
        Aggregated metrics with cancellation rate by group
    """
    metrics = df.groupby(group_by).agg(
        total_flights=('Cancelled', 'count'),
        cancelled_flights=('Cancelled', 'sum')
    ).reset_index()
    
    metrics['cancellation_rate_pct'] = (
        metrics['cancelled_flights'] / metrics['total_flights'] * 100
    )
    
    metrics = metrics.sort_values('cancellation_rate_pct', ascending=False)
    
    return metrics


def compute_average_delay(df, group_by='CarrierName', delayed_only=True):
    """
    Compute average delay magnitude by group.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with flight records
    group_by : str or list
        Column(s) to group by (default: 'CarrierName')
    delayed_only : bool
        If True, only compute for flights with ArrDelay15 = 1 (default: True)
        
    Returns:
    --------
    pd.DataFrame
        Aggregated metrics with average delay by group
    """
    # Filter to delayed flights if requested
    if delayed_only:
        df = df[(df['ArrDelay15'] == 1) & (df['Cancelled'] == 0)].copy()
    else:
        df = df[df['Cancelled'] == 0].copy()
    
    metrics = df.groupby(group_by).agg(
        avg_delay_minutes=('ArrDelayMinutes', 'mean'),
        median_delay_minutes=('ArrDelayMinutes', 'median'),
        max_delay_minutes=('ArrDelayMinutes', 'max'),
        std_delay_minutes=('ArrDelayMinutes', 'std')
    ).reset_index()
    
    metrics = metrics.sort_values('avg_delay_minutes', ascending=False)
    
    return metrics


def create_scorecard(df):
    """
    Create a comprehensive airline scorecard with multiple metrics.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with flight records
        
    Returns:
    --------
    pd.DataFrame
        Comprehensive scorecard with delay rate, cancellation rate, and avg delay
    """
    # Compute individual metrics
    delay_metrics = compute_delay_rate(df)
    cancel_metrics = compute_cancellation_rate(df)
    avg_delay_metrics = compute_average_delay(df)
    
    # Merge into scorecard
    scorecard = delay_metrics[['CarrierName', 'total_flights', 'delay_rate_pct']].copy()
    
    scorecard = scorecard.merge(
        cancel_metrics[['CarrierName', 'cancellation_rate_pct']], 
        on='CarrierName'
    )
    
    scorecard = scorecard.merge(
        avg_delay_metrics[['CarrierName', 'avg_delay_minutes']], 
        on='CarrierName'
    )
    
    # Round for readability
    scorecard['delay_rate_pct'] = scorecard['delay_rate_pct'].round(2)
    scorecard['cancellation_rate_pct'] = scorecard['cancellation_rate_pct'].round(2)
    scorecard['avg_delay_minutes'] = scorecard['avg_delay_minutes'].round(1)
    
    # Sort by delay rate
    scorecard = scorecard.sort_values('delay_rate_pct', ascending=False)
    
    return scorecard


def plot_delay_rates(scorecard, figsize=(12, 6), highlight_worst=True):
    """
    Create a horizontal bar chart of delay rates by airline.
    
    Parameters:
    -----------
    scorecard : pd.DataFrame
        Scorecard dataframe with 'CarrierName' and 'delay_rate_pct' columns
    figsize : tuple
        Figure size (width, height)
    highlight_worst : bool
        If True, highlight the worst performer in red
        
    Returns:
    --------
    matplotlib.figure.Figure
        The figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Sort for visualization (worst at top)
    scorecard_sorted = scorecard.sort_values('delay_rate_pct', ascending=True)
    
    # Create horizontal bar chart
    bars = ax.barh(scorecard_sorted['CarrierName'], scorecard_sorted['delay_rate_pct'], 
                   color='steelblue', edgecolor='black')
    
    # Highlight worst performer
    if highlight_worst:
        worst_idx = scorecard_sorted['delay_rate_pct'].idxmax()
        bars[list(scorecard_sorted.index).index(worst_idx)].set_color('crimson')
    
    # Labels and formatting
    ax.set_xlabel('Delay Rate (%)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Airline', fontsize=12, fontweight='bold')
    ax.set_title('Which Airline Is Most Likely to Make You Late?\\nDelay Rate by Carrier', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Add value labels on bars
    for i, (idx, row) in enumerate(scorecard_sorted.iterrows()):
        ax.text(row['delay_rate_pct'] + 0.3, i, f"{row['delay_rate_pct']:.1f}%", 
                va='center', fontsize=10)
    
    ax.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    
    return fig


def plot_cancellation_rates(scorecard, figsize=(12, 6)):
    """
    Create a horizontal bar chart of cancellation rates by airline.
    
    Parameters:
    -----------
    scorecard : pd.DataFrame
        Scorecard dataframe with 'CarrierName' and 'cancellation_rate_pct' columns
    figsize : tuple
        Figure size (width, height)
        
    Returns:
    --------
    matplotlib.figure.Figure
        The figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    scorecard_sorted = scorecard.sort_values('cancellation_rate_pct', ascending=True)
    
    bars = ax.barh(scorecard_sorted['CarrierName'], scorecard_sorted['cancellation_rate_pct'], 
                   color='coral', edgecolor='black')
    
    ax.set_xlabel('Cancellation Rate (%)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Airline', fontsize=12, fontweight='bold')
    ax.set_title('Flight Cancellation Rate by Carrier', 
                 fontsize=14, fontweight='bold', pad=20)
    
    for i, (idx, row) in enumerate(scorecard_sorted.iterrows()):
        ax.text(row['cancellation_rate_pct'] + 0.05, i, f"{row['cancellation_rate_pct']:.2f}%", 
                va='center', fontsize=10)
    
    ax.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    
    return fig


def plot_delay_vs_cancellation(scorecard, figsize=(10, 7)):
    """
    Create a scatter plot of delay rate vs. cancellation rate.
    
    Parameters:
    -----------
    scorecard : pd.DataFrame
        Scorecard with 'CarrierName', 'delay_rate_pct', and 'cancellation_rate_pct'
    figsize : tuple
        Figure size (width, height)
        
    Returns:
    --------
    matplotlib.figure.Figure
        The figure object
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.scatter(scorecard['delay_rate_pct'], scorecard['cancellation_rate_pct'], 
               s=200, alpha=0.6, c='steelblue', edgecolors='black', linewidth=1.5)
    
    # Add airline labels
    for idx, row in scorecard.iterrows():
        ax.annotate(row['CarrierName'], 
                    (row['delay_rate_pct'], row['cancellation_rate_pct']),
                    xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    ax.set_xlabel('Delay Rate (%)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Cancellation Rate (%)', fontsize=12, fontweight='bold')
    ax.set_title('Airline Reliability: Delay Rate vs. Cancellation Rate', 
                 fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return fig


def print_summary_stats(df):
    """
    Print summary statistics for the dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with flight records
    """
    print("="*80)
    print("DATASET SUMMARY STATISTICS")
    print("="*80)
    print(f"Total flights: {len(df):,}")
    print(f"Airlines: {df['CarrierName'].nunique()}")
    print(f"Date range: {df['Year'].min()}-{df['Month'].min():02d} to {df['Year'].max()}-{df['Month'].max():02d}")
    print(f"\nOverall Metrics:")
    print(f"  - Delay rate (≥15 min): {df['ArrDelay15'].mean() * 100:.2f}%")
    print(f"  - Cancellation rate: {df['Cancelled'].mean() * 100:.2f}%")
    
    df_completed = df[df['Cancelled'] == 0]
    if 'ArrDelayMinutes' in df.columns:
        delayed = df_completed[df_completed['ArrDelay15'] == 1]
        if len(delayed) > 0:
            print(f"  - Avg delay (for delayed flights): {delayed['ArrDelayMinutes'].mean():.1f} minutes")
    
    print("="*80)


def identify_worst_performers(scorecard, n=3):
    """
    Identify the worst performing airlines by delay rate.
    
    Parameters:
    -----------
    scorecard : pd.DataFrame
        Scorecard with airline metrics
    n : int
        Number of worst performers to return (default: 3)
        
    Returns:
    --------
    pd.DataFrame
        Top n worst performers
    """
    worst = scorecard.nlargest(n, 'delay_rate_pct')
    
    print(f"\n🔴 TOP {n} AIRLINES MOST LIKELY TO MAKE YOU LATE:")
    print("="*60)
    for idx, row in worst.iterrows():
        rank = list(worst.index).index(idx) + 1
        print(f"{rank}. {row['CarrierName']:<25} {row['delay_rate_pct']:.2f}% delay rate")
    print("="*60)
    
    return worst


def identify_best_performers(scorecard, n=3):
    """
    Identify the best performing airlines by delay rate.
    
    Parameters:
    -----------
    scorecard : pd.DataFrame
        Scorecard with airline metrics
    n : int
        Number of best performers to return (default: 3)
        
    Returns:
    --------
    pd.DataFrame
        Top n best performers
    """
    best = scorecard.nsmallest(n, 'delay_rate_pct')
    
    print(f"\n🟢 TOP {n} MOST RELIABLE AIRLINES:")
    print("="*60)
    for idx, row in best.iterrows():
        rank = list(best.index).index(idx) + 1
        print(f"{rank}. {row['CarrierName']:<25} {row['delay_rate_pct']:.2f}% delay rate")
    print("="*60)
    
    return best


def check_data_quality(df):
    """
    Perform data quality checks and report issues.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with flight records
    """
    print("\n" + "="*80)
    print("DATA QUALITY CHECK")
    print("="*80)
    
    # Missing values
    print("\n1. Missing Values:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing Count': missing,
        'Percentage': missing_pct
    })
    problem_cols = missing_df[missing_df['Missing Count'] > 0]
    if len(problem_cols) > 0:
        print(problem_cols.sort_values('Missing Count', ascending=False))
    else:
        print("   ✅ No missing values found")
    
    # Duplicate rows
    print("\n2. Duplicate Rows:")
    dups = df.duplicated().sum()
    print(f"   Total duplicates: {dups:,} ({dups/len(df)*100:.2f}%)")
    
    # Value ranges
    print("\n3. Value Range Checks:")
    if 'ArrDelay15' in df.columns:
        invalid_delay15 = df[~df['ArrDelay15'].isin([0, 1, np.nan])]['ArrDelay15'].count()
        print(f"   - Invalid ArrDelay15 values (not 0/1): {invalid_delay15}")
    
    if 'Cancelled' in df.columns:
        invalid_cancelled = df[~df['Cancelled'].isin([0, 1, np.nan])]['Cancelled'].count()
        print(f"   - Invalid Cancelled values (not 0/1): {invalid_cancelled}")
    
    print("="*80)


# Example usage (for testing)
if __name__ == "__main__":
    print("Airline Delay Analysis Helper Functions")
    print("Import this module in your Jupyter notebook to use these functions.")
    print("\nExample:")
    print("  from helper_functions import load_and_validate_data, create_scorecard")
    print("  df = load_and_validate_data('../DATA/airline_delays_2022_2024.csv')")
    print("  scorecard = create_scorecard(df)")

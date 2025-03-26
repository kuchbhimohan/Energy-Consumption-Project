import pandas as pd

def show_missing_values(df, show_percentage=False, sort_results=False, return_results=False):
    """
    Analyze and display missing values in a DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Input DataFrame to analyze
    show_percentage : bool, optional
        If True, shows percentage of missing values (default: False)
    sort_results : bool, optional
        If True, sorts results by missing count descending (default: False)
    return_results : bool, optional
        If True, returns the results DataFrame (default: False)
        
    Returns:
    --------
    pandas.DataFrame or None
        Returns results if return_results=True, otherwise None
    """
    # Calculate missing values
    missing_counts = df.isna().sum()
    total_rows = len(df)
    
    # Create results DataFrame
    results = pd.DataFrame({'Missing Count': missing_counts})
    
    if show_percentage:
        results['Missing (%)'] = (missing_counts / total_rows * 100).round(2)
    
    if sort_results:
        results = results.sort_values('Missing Count', ascending=False)
    
    # Display results
    print("="*50)
    print("MISSING VALUES ANALYSIS")
    print("="*50)
    print(results)
    print("\nTotal rows in dataset:", total_rows)
    print("="*50)
    
    if return_results:
        return results
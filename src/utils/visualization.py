# src/utils/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column_name, bins=50, figsize=(10, 6), edgecolor='black',
                  title=None, xlabel=None, ylabel='Frequency', grid=True,
                  color='skyblue', kde=False, ax=None):
    """
    Enhanced histogram plotting function with more options.
    
    Parameters:
    -----------
    kde : bool
        Whether to add KDE line (uses seaborn if True)
    ax : matplotlib.Axes, optional
        If provided, plots on this axis instead of creating new figure
    """
    data = df[column_name].dropna()
    
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.get_figure()
    
    if kde:
        sns.histplot(data, bins=bins, edgecolor=edgecolor, color=color,
                    kde=True, ax=ax)
    else:
        ax.hist(data, bins=bins, edgecolor=edgecolor, color=color)
    
    ax.set_title(title if title is not None else f'Distribution of {column_name}')
    ax.set_xlabel(xlabel if xlabel is not None else column_name)
    ax.set_ylabel(ylabel)
    ax.grid(grid)
    
    if ax is None:
        plt.tight_layout()
        plt.show()
    
    return fig, ax


def plot_categorical_bar(data, column, title=None, xlabel=None, ylabel="Count", palette="viridis", 
                       figsize=(8, 5), annotate=True, rotate_xlabels=False, horizontal=False):
    """
    Plots and returns a bar chart for a categorical column.
    
    Parameters:
    - data: pandas DataFrame
    - column: Name of the categorical column
    - title: Plot title (default: f"Bar Plot of {column}")
    - xlabel: X-axis label (default: column name)
    - ylabel: Y-axis label (default: "Count")
    - palette: Color palette (default: "viridis")
    - figsize: Figure size (default: (8, 5))
    - annotate: Add count labels on bars (default: True)
    - rotate_xlabels: Rotate x-axis labels (default: False)
    - horizontal: Plot horizontal bars (default: False)
    
    Returns:
    - matplotlib.axes.Axes: The Axes object for further customization.
    """
    counts = data[column].value_counts()
    
    if title is None:
        title = f"Bar Plot of {column}"
    if xlabel is None:
        xlabel = column

    fig, ax = plt.subplots(figsize=figsize)
    
    if horizontal:
        sns.barplot(x=counts.values, y=counts.index, palette=palette, ax=ax)
        if annotate:
            for i, v in enumerate(counts.values):
                ax.text(v + 0.2, i, str(v), color='black')
    else:
        sns.barplot(x=counts.index, y=counts.values, palette=palette, ax=ax)
        if annotate:
            for i, v in enumerate(counts.values):
                ax.text(i, v + 0.2, str(v), ha='center', color='black')
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if rotate_xlabels:
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    return ax
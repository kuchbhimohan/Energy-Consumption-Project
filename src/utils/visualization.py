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
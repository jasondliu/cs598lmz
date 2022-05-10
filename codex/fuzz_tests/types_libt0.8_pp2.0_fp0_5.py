import types
types.SimpleNamespace()

import pylab

def plot_outcome_distribution(dataset, ax):
    """Plot the distribution of outcomes for a given dataset."""
    outcomes = dataset["outcome"].value_counts()
    outcomes.plot(kind="bar", ax=ax, sort_columns=True)
    return outcomes

def plot_outcome_over_time(data, ax):
    pass

def plot_outcome_distribution_by_partner(dataset, ax):
    """Plot the distribution of outcomes by partner."""
    # List of unique partners
    partners = dataset["company_name"].unique()

    # Choose the colors.
    colors = pylab.cm.Spectral(pylab.np.linspace(0, 1, len(partners)))

    # Plot the outcome distribution for each partner.
    dist = dataset["outcome"].value_counts()
    dist_by_partner = dataset.groupby("company_name")["outcome"].value_counts()
    for p, c, n in

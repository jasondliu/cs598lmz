import weakref
import weakref
import mcviz_tools as mcv
# import simulator as sim
# reload(sim)
import sim_tools as sim
reload(sim)
import ipywidgets
import collections
import math
import numpy as np
import scipy.stats
import matplotlib.pylab as plt
import seaborn as sns


# Plotting functions
def plot_cumulative_degree(mixed_outs, sample_sizes=None, **kwargs):
    sns.set(font_scale=2)
    # TODO: sample_sizes should be set to the number of ballots.
    sample_size = kwargs.pop('sample_size', None)
    if 'plot_deg_dist' in kwargs.keys():
        plot_deg_dist = kwargs.pop('plot_deg_dist')
    else:
        plot_deg_dist = True

    if 'right_margin' in kwargs.keys():
        right_margin = kwargs.pop('right_margin')
    else:
        right_margin

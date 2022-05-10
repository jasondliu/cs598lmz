import ctypes
ctypes.windll.user32.SetProcessDPIAware()

# Main imports
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import random

# What are we going to plot?
fontsize = 14
plt.rcParams.update({'font.size': fontsize})

dist_names = ['norm','gamma','beta']

# Create distribution objects
N = stats.norm()
G = stats.gamma(3)
B = stats.beta(3,3)

# Plot distributions
fig, ax = plt.subplots(1,1)

x = np.linspace(N.ppf(0.01), N.ppf(0.99), 100)
ax.plot(x, N.pdf(x), 'k-', lw=5, label=u'norm pdf')
ax.plot(x, G.pdf(x), 'b-', lw=2, alpha=0.6, label=u'gamma pdf')


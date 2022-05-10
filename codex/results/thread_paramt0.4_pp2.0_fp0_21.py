import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()

# Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.optimize as opt

# Import custom modules
import model
import data
import fit

# Load data
data = data.load_data()

# Set up model
model = model.Model(data)

# Fit model
fit = fit.Fit(model)
fit.fit()

# Plot results
fit.plot()

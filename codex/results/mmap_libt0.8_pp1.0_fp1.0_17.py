import mmap
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import median_filter
### Edit the path to the data.

data_folder = 'C:\Users\Tim\Documents\PhD\GRS1915_timing'
data_file = 'GRS1915-105_QPO_rxte_xte_pca_13.txt'
data_path = os.path.join(data_folder,data_file)

### The bin size for the power spectra (logarithmic, for each decade)

bin_size = 1./512.

### The frequency range over which to fit the power law in the power spectra

fit_range = [2,100]

### The maximum frequency for the rebinning in the logarithm

max_freq = fit_range[1]*1.1

### The number of times the power law is averaged to obtain the best fit parameters

fit_steps = 10

### The number of steps by which the power law is shifted to obtain the best fit parameters

shift_steps

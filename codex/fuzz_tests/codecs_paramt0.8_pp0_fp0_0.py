import codecs
codecs.register_error('surrogatescape', codecs.surrogateescape_error)

from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 2:
    print("Usage: python3 plot_calibration.py <mat file>")
    print("    where <mat file> is a file output by the matlab script")
    sys.exit(1)

filename = sys.argv[1]

mat = loadmat(filename)

data = mat['data']

data = data.T

for i in range(16):
    xi = data[:, i]
    xi = xi[ np.logical_not( np.isnan(xi)) ]
    print(np.mean(xi), np.std(xi))

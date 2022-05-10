import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from scipy.signal import find_peaks_cwt
from scipy.signal import peak_widths
from scipy.signal import peak_prominences
from scipy.signal import savgol_filter
from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import CubicSpline
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.interpolate import Akima1DInterpolator
from scipy.interpolate import PchipInterpolator
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import KroghInterpolator
from scipy.interpolate import PiecewisePolynomial

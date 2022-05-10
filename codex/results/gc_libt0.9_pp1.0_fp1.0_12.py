import gc, weakref
from scipy.optimize import curve_fit, least_squares
from functions import *
from functools import partial


def fit_transmission(wl, trans, plot=False, interp=False):
    """
    fit transmission, given an array of wl, trans
    
    example:
        wl = np.linspace(10000, 11000, 50)
        trans = 2*(np.sin(wl-np.floor(wl/100)*100)**2)+1
        plot = False # plot the fit result
        fit_transmission(wl, trans, plot)
    """
    if plot:
        plt.plot(wl, trans)
    
    # get rough transmission windows
    interpfunc = interp1d(wl, trans, kind='cubic', fill_value="extrapolate")
    wl_interp = np.linspace(wl.min(), wl.max(), 500)
    trans = interpfunc(wl_interp)
    # find minimum
    freqs = np.linspace(1, 5, 100)


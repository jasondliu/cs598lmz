import ctypes
ctypes.cdll.LoadLibrary('./hacklib.so')
import demo
print(demo.add(1, 2))

import matplotlib.pyplot as plt

def histogram(img, window=None, level=None):
    """
    calculates a histogram of a given image,
    
    :param window: upper and lower bounds of window level, following the format (level, window)
    :type window: tuple
    :return: plot of histogram
    :rtype: matplotlib plot
    """
    
    return

def gaussianfilter(img, window=None, level=None):
    """
    creates a gaussian-filtered version of a given image.
    
    
    :param window:
    :type window:
    :param level:
    :type level:
    :param settings:
    :type settings:
    :return:
    :rtype:
    """
    
    return

def inversefilter(img, window=None, level=None):
    """
    creates a gaussian-filtered version of a given image

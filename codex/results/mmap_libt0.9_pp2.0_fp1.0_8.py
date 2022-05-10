import mmap
import random
import time

import numpy as np
import pandas as pd


class EDMatrix(object):
    """
    Object containing similarity matrix and a variety of formats
    """
    def __init__(self, matrix, index=None, columns=None, data_type=None):
        self.matrix = matrix
        self.index = index
        self.columns = columns
        self.data_type = data_type


def find_nearest(array, value):
    """
    Finds the index of the closest value in an array
    :param array: 1-dim array
    :param value:
    :return:
    """
    n = [abs(i - value) for i in array]
    idx = n.index(min(n))
    return idx


def peak_detection(data, mph=None, mpd=1, threshold=0, edge='rising',
                   kpsh=False, valley=False, show=False, ax=None):
    """Peak detection routine.
    Adapted from Nedrow et al.

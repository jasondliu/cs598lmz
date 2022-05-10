import gc, weakref
import numpy as np

#_______________________________________________________________________________
class DataPoint(object):

  '''Instances of this class are returned by
  :py:class:`Forest.bestSplitPoints` when it encounters a univariate data
  point.  If a multivariate split point is encountered, the parameters of
  :py:class:`DataPoint` are lists of the same length as
  :py:data:`Forest.nd`.

  Attributes
  ----------
  axis : int or list of int
    Axis along which this point is split.
  index : int or list of int
    Index of this point in the data set.
  thresh : float or list of float
    Threshold of this point.
  '''

  def __init__(self, axis, index, thresh):
    '''
    Parameters
    ----------
    axis : int or list of int
      Axis along which this point is split.
    index : int or list of int
      Index of this point in the data set.
    thresh : float or list of float
      Threshold at which this point is split.


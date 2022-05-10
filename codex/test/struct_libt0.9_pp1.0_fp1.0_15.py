import _struct
from _collections import defaultdict
from functools import reduce
from StringIO import StringIO
import numpy

from UserDict import DictMixin

from nipype.utils.misc import str2bool

class Bunch(object):
    """ Dummy class for storing attributes

    Examples
    --------

    >>>
    >>> b = Bunch(a=1, b=2)
    >>> b.a
    1
    >>> b['b']
    2
    >>> b.update({'b': 3, 'c': 4})
    >>>
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return str(self.__dict__)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __delitem__(self, key):
        del self.__dict__[key]

   

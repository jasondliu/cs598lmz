import weakref
import warnings
import numpy

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

_DEBUG = False

#-----------------------------------------------------------------------------
# Classes and functions
#-----------------------------------------------------------------------------

class VtkBase(object):
    '''
    Wraps around a VTK object and provides a simpler interface. It is a helper
    class for VtkData.

    .. Note::
        VtkBase is not used directly by the user.
    '''

    def __init__(self, obj, data_manager=None):
        self._obj = obj
        self._data_manager = data_manager

    def __getattr__(self, name):
        if hasattr(self._obj, name):
            return getattr(self._obj, name)
        raise AttributeError("'%s' not found" % name)

    def __setattr__(self, name, value):
        if name == '_data_manager' and isinstance(value, VtkData):
            self._data_manager = weakref.ref(value)
        elif name == '_obj':
            self

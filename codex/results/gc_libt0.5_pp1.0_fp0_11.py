import gc, weakref
from . import _py2to3

#-------------------------------------------------------------------------------
#  'WeakValueDictionary' class:
#-------------------------------------------------------------------------------

class WeakValueDictionary ( object ):
    """A dictionary with weak values.

    This is a dictionary that keeps weak references to its values.  When
    a value is no longer referenced, it is automatically removed from the
    dictionary.

    """

    def __init__ ( self, dict = None ):
        """Initialize the dictionary with optional contents.

        dict is a dictionary whose contents are copied into the new
        WeakValueDictionary.  If dict is not provided, an empty
        WeakValueDictionary is created.

        """
        if dict is None:
            dict = {}
        self.data = {}
        for key, value in dict.items():
            self[key] = value


    def __getitem__ ( self, key ):
        """Get an item from the dictionary."""
        return self.data[key][0]()


    def __setitem__ ( self, key, value ):
        """Set an item in the dictionary."""
        self.

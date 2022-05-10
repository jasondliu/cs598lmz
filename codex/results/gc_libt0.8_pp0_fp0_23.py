import gc, weakref
import numpy as np

from isaac.tools import *

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
class PersistentDictionary_Error( Exception ):
    """
    An exception raised by PersistentDictionary class.
    """

    def __init__( self, msg ):
        self.msg = msg

    def __str__( self ):
        return self.msg


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
class PersistentDictionary( dict ):
    """
    A dictionary that remembers keys when clear() is called.

    This class caches the keys, i.e. "persists" them.
    """

    def __init__( self, *args, **kwargs ):

        dict.__init__( self, *args, **kwargs )
        self._keys = []


    def __setitem__( self, key, value ):

        dict.__setitem__( self, key, value )

        if key not in self._keys:
            self._keys.append( key )


    def clear( self ):

        for key in self._keys:
           

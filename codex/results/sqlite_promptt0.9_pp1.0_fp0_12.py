import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect:
import LuaState

class LuaLibBase(object):
    """
    Helper class that implements static methods to load Lua libraries,
    i.e. all functions defined in liblua so that they are available to
    client scripts that create a new Lua state.
    """

    def __init__(self, **kwargs):
        """Initialise a new library object."""
        # Call the super class constructor:
        super(LuaLibBase, self).__init__(**kwargs)
        # Load the appropriate library:
        self.lib = ctypes.cdll.LoadLibrary(self.libname)
        # Set types for all library functions:
        self.setup_types()

    @property
    def libname(self):
        """Return the name of the library library as string."""
        libname = 'liblua.so'
        try:
            # Find the library:
            return ctypes.util.find_library(libname)
        except Exception, e:
            # We failed, not supported platform perhaps?
            raise NotImplementedError('Unable to load the

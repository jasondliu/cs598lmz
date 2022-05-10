import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time

#
# This is a simple example of how to use the libtrace library to
# read a trace file and print out the contents of the packets to
# stdout.
#

# The libtrace library is split into two parts -- the core library
# and the IO module.  The core library provides all of the
# functionality for dealing with trace formats, trace files, packets
# etc.  The IO module provides the ability to read and write packets
# to various types of trace sources.
#
# The IO module is implemented as a shared library that is loaded
# dynamically at runtime.  This allows us to use the same core
# library for reading and writing traces without having to link
# against all of the IO modules.
#
# The following code is used to load the IO module and initialise the
# libtrace library.  The IO module is loaded using ctypes.util.find_library
# which will search the standard library paths for the shared library
# and return the full path to it.  If the library cannot be found,
# find_library will return None.
#
# The

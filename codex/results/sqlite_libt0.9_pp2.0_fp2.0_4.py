import ctypes
import ctypes.util
import threading
import sqlite3
from datetime import datetime
from datetime import timedelta

# This is a set of script interfaces that allow you to control the ImageProperties processor
# These utilities depend on libImageProperties.so and its header file, which must be compiled and 
# installed in appropriate locations

# This module automatically loads the library from the default path
# If necessary, use LD_LIBRARY_PATH to direct the library loader appropriately
# I do this automatically by running
# export LD_LIBRARY_PATH=/home/nadine/qserv/qserv/ImageProperties/lib/:$LD_LIBRARY_PATH
# but you may have to do this and may have to do it differently

try:
    # load in the library via the ctypes interface
    import os
    lib = ctypes.CDLL(os.environ["HOME"]+"/qserv/qserv/ImageProperties/lib/libImageProperties.so")
except KeyError:
    print "Could not find Home environment variable. Quitting"
    sys.exit(1)
    

# this is the type definition for the

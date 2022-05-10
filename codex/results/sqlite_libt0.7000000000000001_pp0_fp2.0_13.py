import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time

# Set up our variables

# This is the path to the libstdc++.so library that is used by the
# vlc libvlc.so library.
if sys.platform == 'darwin':
    libvlc_path = os.path.join(os.path.expanduser('~'), 'vlc', 'lib', 'libvlc.dylib')
    libstdcpp_path = os.path.join(os.path.expanduser('~'), 'vlc', 'lib', 'libstdc++.6.dylib')
else:
    libvlc_path = ctypes.util.find_library('vlc')
    libstdcpp_path = ctypes.util.find_library('stdc++')

if not libvlc_path:
    raise Exception("Can't find the required vlc library")

if not libstdcpp_path:
    raise Exception("Can't find the required stdc++ library")

# We need to load the stdc++ library before we load the vlc library.
#

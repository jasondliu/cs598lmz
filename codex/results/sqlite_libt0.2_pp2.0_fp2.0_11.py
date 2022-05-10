import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime
import re
import urllib
import urllib2
import json
import traceback

#
# The following is a hack to get around the fact that the
# Python ctypes module doesn't support the "const" keyword
# in function declarations.
#
# This is a problem because the libspotify API uses the
# "const" keyword in a lot of places.
#
# The hack is to replace the "const" keyword with "__const__"
# in the libspotify header files.
#
# Then, after the header files have been loaded, we replace
# all instances of "__const__" with "const" in the loaded
# header files.
#
# This allows us to use the "const" keyword in our Python
# code, and the ctypes module will be none the wiser.
#

#
# Replace all instances of "__const__" with "const" in the
# libspotify header files.
#
def fix_libspotify_header_files():
    for filename in os.listdir("libspot

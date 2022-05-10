import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import re
import socket

# Stuff we need to get
# * Titles, ids, and descriptions of all feeds
# * Titles, ids, and descriptions of all podcasts in all feeds
# * Titles, ids, and descriptions of all episodes in all podcasts
# * Download status of all episodes

# Apparently, there is no easy way to get a list of all feeds,
# but there is an easy way to find out how many there are.
# This is done by calling "CFRunLoopRunInMode(kCFRunLoopDefaultMode,
# 0.005, false);" and then using the feed count function.
# Now, we can simply loop over all the feeds and get their properties.
# This does, however, require us to have a CFRunLoop to use.
# This is also what we need in order to get the properties of all
# podcasts, since we will have to loop over them and get their
# properties.  Unfortunately, the only way I've found to do that
# is to create a CFRunLoopSource, give it the podcast list, and
# add it

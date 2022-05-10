import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
# on different platforms.

# http://www.sqlite.org/sharedcache.html

# Needs to be run with -O (optimize) python option.

# On Linux pthread_create is called via a symlink in libpthread.so
# and libpthread.so is a symlink to libpthread-2.11.so
#
# ls -l /lib/libpthread*
# lrwxrwxrwx. 1 root root 13 2012-05-04 08:21 /lib/libpthread-2.11.so -> libpthread.so.0
# lrwxrwxrwx. 1 root root 13 2012-03-30 18:11 /lib/libpthread.so -> libpthread-2.11.so
# -rwxr-xr-x. 1 root root 163312 2012-05-04 08:21 /lib/libpthread.so.0
#
# The symlink is needed to make ctypes.util.find_library() work,
# but this is not

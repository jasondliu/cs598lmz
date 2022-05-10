import ctypes
import ctypes.util
import threading
import sqlite3


# -----------------------------------------------------------------------------
#   Constants.
# -----------------------------------------------------------------------------

# There's no way to detect whether a module is being run normally,
# or if it's being run by a doctest, so we randomly pick a port number
# to run on, and if that port happens to be in use, we assume we're
# being run by a doctest and try the next one.
#
# This is a list of ports to try.
port_range = [8221, 8222, 8223, 8224, 8225]

# The host name to bind to.
host = '127.0.0.1'

# The default page returned.
default_page = 'index.html'

# The file extensions and their associated MIME types.
extensions_map = {
    '': 'application/octet-stream',  # Default
    '.py': 'text/plain',
    '.c': 'text/plain',
    '.h': 'text/plain',
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'application/x-

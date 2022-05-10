import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect("file:memdb?mode=memory&cache=shared")
# Test sqlite3.connect("file::memory:?cache=shared")
# Test sqlite3.connect("file::memory:", uri=True)

# Test the sqlite3.connect() database URI filename interpretation
#
# Spec:
#
#  1. If URI filename interpretation is enabled, and the filename argument
#     begins with "file:", then the filename is interpreted as a URI.
#  2. A URI filename is made up of a scheme, authority, and path,
#     similar to the generic URI syntax (RFC 3986). The scheme and
#     authority components are optional. If either the scheme or
#     authority component are present, then both scheme and authority
#     must be present. The path component is required.
#  3. The scheme name must be either "file", "file+unixsocket",
#     "file+zip", or "file+zipserver".
#  4. If the scheme is "file+unixsocket" then the filename is interpreted

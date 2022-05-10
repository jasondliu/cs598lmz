import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys

# This is a simple program to get the current time from a GPS device
# and store it in a database. This can be used to synchronize the
# system clock with the GPS clock.

# The program uses the gpsd library to talk to the gps device.
# The gpsd library is available from http://www.catb.org/gpsd/
# The gpsd library is available from the Debian package gpsd-clients

# The program uses the gps library to read the current time from the gps device.
# The gps library is available from the Debian package python-gps

# The program uses the sqlite3 library to store the time in a database.
# The sqlite3 library is available from the Debian package python-sqlite

# The program uses the ctypes library to execute a system call to set the system clock.
# The ctypes library is available from the Debian package python-ctypes

# The program uses the ctypes.util library to execute a system call to set the system clock.
# The ctypes.util library is available from the

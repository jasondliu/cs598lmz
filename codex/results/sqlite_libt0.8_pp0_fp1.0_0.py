import ctypes
import ctypes.util
import threading
import sqlite3
import base64
import struct
import binascii
import datetime
import json
import socket

#
# The following is from: http://bugs.python.org/issue7980
#

# This code requires Python 2.6 or higher.
# This code requires the ctypes module, which is in the standard library
# for Python 2.5 and up.

# This code is derived from the _curses module in Python's source code.
# That code is under the Python license:
#
# Python license
#
# Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
# 2011, 2012, 2013, 2014, 2015 Python Software Foundation;
# All Rights Reserved
#
# PSF license AGREEMENT FOR PYTHON 2.1.1
#
# 1. This LICENSE AGREEMENT is between the Python Software Foundation
# ("PSF"), and the Individual or Organization ("Licensee") accessing and
# otherwise using this software ("Python") in source or binary form and
# its associated documentation.
#
# 2. Subject to the terms and

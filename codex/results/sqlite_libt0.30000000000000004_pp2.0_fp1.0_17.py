import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time
import sys

from .constants import *
from .exceptions import *
from .utils import *

# Load the libspotify library
libspotify = ctypes.CDLL(ctypes.util.find_library('spotify'))

# Set the libspotify library to return None instead of NULL
# for functions that return pointers
libspotify.sp_session_user_name.restype = ctypes.c_char_p
libspotify.sp_session_canonical_username.restype = ctypes.c_char_p
libspotify.sp_session_display_name.restype = ctypes.c_char_p
libspotify.sp_session_remembered_user_name.restype = ctypes.c_char_p
libspotify.sp_session_user_country.restype = ctypes.c_char_p
libspotify.sp_session_remembered_user_password.restype = ctypes.c_char_p
libspotify.sp_session_remembered_remembered_

import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import datetime
import random
import re
import math
import traceback

# This is the interface to the C library
_lib = ctypes.CDLL(ctypes.util.find_library('sensors'))

# This is a list of all the sensors that we know about
_sensors = []

# This is a list of all the chip names that we know about
_chips = []

# This is a list of all the subfeature names that we know about
_subfeatures = []

# This is a list of all the bus names that we know about
_busses = []

# This is a list of all the adapters that we know about
_adapters = []

# This is a list of all the labels that we know about
_labels = []

# This is a list of all the types that we know about
_types = []

# This is a list of all the features that we know about
_features = []

# This is a list of all the subfeatures that we know about
_subfeatures = []

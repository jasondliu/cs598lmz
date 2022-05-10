import ctypes
ctypes.cast(0, ctypes.py_object)

# imports
import sys
import os
import importlib
import pickle

# import my own modules
import lib.lib_database as lib_database
import lib.lib_log as lib_log
import lib.lib_data as lib_data
import lib.lib_image as lib_image

# import constants
import config.const_database as const_database
import config.const_general as const_general

# import variables
import config.var_database as var_database
import config.var_general as var_general

# import settings
import config.settings_database as settings_database
import config.settings_general as settings_general

# import functions
import config.settings_functions as settings_functions

# import classes
import config.settings_classes as settings_classes

# import objects
import config.settings_objects as settings_objects

# import libraries
import config.settings_libraries as settings_libraries

# import frameworks
import config.settings_frameworks as settings_frameworks


# function to get a specific module from

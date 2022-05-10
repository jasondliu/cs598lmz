import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import time
import dateutil.parser as dparser

import sys
import os

import imp
import inspect

# sys.path.append("/home/travis/build/mattfried/botbot-plugins/plugins/")
# print sys.path

# from plugins.test import plugin_test

# print plugin_test.__name__
#
# # print inspect.getsource(plugin_test)
# # print inspect.getsource(plugin_test.test)
# print inspect.getsource(plugin_test.test_silly)

# sys.path.append("/home/travis/build/mattfried/botbot-plugins/plugins")
# mod_name_to_load = "test"
# full_path = os.path.join("/home/travis/build/mattfried/botbot-plugins/plugins", mod_name_to_load)
# print full_path
# mod_to_load = imp.load_source(mod_name_to_load, full_path)
# print mod_to_load

# import test

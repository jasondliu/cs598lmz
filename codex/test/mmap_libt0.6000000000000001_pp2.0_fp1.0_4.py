import mmap
import os
import re
import shutil
import string
import sys
import tempfile
import time
import types
import unittest
import warnings

# If a test is failing, you can add the line
#    print_debug = True
# in the test method to get a log of what is happening.
# This will print the commands being run and the output
# of those commands.
print_debug = False

# Some tests require the use of the network and some
# tests are designed to run faster when the network
# is not used.  These tests will use the network by
# default, but can be run without the network by
# setting the 'no_network' variable to True.
no_network = False

# The following variables are set in setUp() and
# can be used by tests that need to know the test
# environment.
wc_dir = None
svntest.main.temp_dir = None

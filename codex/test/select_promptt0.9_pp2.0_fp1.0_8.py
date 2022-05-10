import select
# Test select.select for use.
t_run.t_select == select.__name__

import mysocket_unit
# The unittest is still called here because t_run is a module itself, so
# __init__ is never called automatically. 
t_run.t_run()

# Content of test_msocket.py:

# Importing msocket, as well as the unittest module.
# Import sys to exit after 1 test case, and also to be ready to pass
# command line arguments to this script.
from mysocket import *
import unittest
import sys
global t
global test_ok
test_ok = True

# Method to assert equality of the outputs from the next 2 calls of  
# mysocket.connect, and also test that the connection is successful.
def test_connect(self):
    r = msocket.connect()
    if (r == False):
        self.assertEqual(msocket.connect(), r)

# Method to test separating messages correctly.

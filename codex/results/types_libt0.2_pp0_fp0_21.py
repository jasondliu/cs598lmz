import types
types.ClassType = type

import unittest
import sys
import os

from test import test_support

# Skip test if _tkinter wasn't built.
test_support.import_module('_tkinter')

from Tkinter import Tcl, Tk, TclError
from _tkinter import Tcl_Obj

# Tcl_Obj.string is a read-only attribute, so we need to use this
# function to set it.
def set_tcl_obj_string(obj, string):
    obj.string = string

class TkinterTest(unittest.TestCase):

    def setUp(self):
        self.interp = Tcl()
        self.tk = Tk(self.interp)
        self.addCleanup(self.tk.destroy)
        self.addCleanup(self.interp.destroy)

    def testTk(self):
        # test that Tk() works at all
        self.assertEqual(self.tk.winfo_name(), '.!frame')

    def testTcl(self):
       

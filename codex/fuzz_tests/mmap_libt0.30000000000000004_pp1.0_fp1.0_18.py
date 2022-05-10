import mmap
import os
import re
import struct
import sys
import tempfile
import time
import traceback
import types
import unittest

import lldb
from lldbsuite.test.decorators import *
from lldbsuite.test.lldbtest import *
from lldbsuite.test import lldbutil


class TestCase(TestBase):

    mydir = TestBase.compute_mydir(__file__)

    def setUp(self):
        # Call super's setUp().
        TestBase.setUp(self)
        # Find the line number to break inside main().
        self.line = line_number('main.cpp', '// Set break point at this line.')

    @add_test_categories(['pyapi'])
    def test_with_python_api(self):
        """Test SBTarget.BreakpointCreateByLocation with Python APIs."""
        self.build()
        exe = os.path.join(os.getcwd(), "a.out")

        # Create a target by the debugger.
       

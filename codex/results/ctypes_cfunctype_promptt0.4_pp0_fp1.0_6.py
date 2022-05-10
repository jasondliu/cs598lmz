import ctypes
# Test ctypes.CFUNCTYPE()

# Initialize ctypes
import ctypes
from ctypes import *

# Initialize Numpy
import numpy

# Test and time libraries
import time
import unittest

# Import the check_err and check_err_warn  functions
from cudamat_conv import check_err, check_err_warn

# Import the GPU functions
from cudamat_conv import *

# Import the Python float type
from numbers import Number

# Import the Python int type
from numbers import Integral

# Import the Python long type
from numbers import Integral

# Import the Python bool type
from numbers import Boolean

# Test the GPU functions
class TestCudamatConv(unittest.TestCase):

    def test_cudamat_conv_convUp_1(self):
        """
        Test function convUp(self, A, B, C, d, p, s, b)
        """
        print('Testing function convUp(self, A, B, C, d, p, s, b)')

        # Initialize ctypes


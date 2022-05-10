import ctypes
# Test ctypes.CFUNCTYPE() by calling a function like this in a main()
# function:
#
#     def func(a, b, c):
#         print a, b, c
#     c_func = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int,
#                                    ctypes.c_int)(func)
#     c_func(1, 2, 3)

# This file is part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

import unittest
import os


class TestCtypes(unittest.TestCase):
    def test_CFUNCTYPE(self):
        try:
            import ctypes
        except ImportError:
            # Python 2.6 doesn't have ctypes, so just skip this test.
            return


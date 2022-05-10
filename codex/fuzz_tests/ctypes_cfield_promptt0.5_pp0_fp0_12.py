import ctypes
# Test ctypes.CField.

# This file is part of Cython.
#
# Cython is free software: you can redistribute it and modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cython is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cython.  If not, see <http://www.gnu.org/licenses/>.

# The original test file is part of the Python 2.7.3 distribution.
# It is Copyright (c) 2001-2012 Python Software Foundation; All Rights Reserved
# and is included as a component of Python.  The original file is licensed
# under the PSF License Agreement.

import unittest
from test import test_support

class CFieldTest(

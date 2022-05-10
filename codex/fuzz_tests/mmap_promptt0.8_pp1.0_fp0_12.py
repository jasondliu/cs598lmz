import mmap
# Test mmap.mmap vs numpy.memmap for reading binary files
#
#
# Copyright (C) 2015  Zhe Liu <liuzhebusiness@gmail.mmap>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
import numpy as np
import time
import sys
import os

# -----------------------------------------------------------------------------
# read test file with mmap class
# -----------------------------------------------------------------------------
def readmmap(fp

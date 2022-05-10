import mmap
# Test mmap.mmap()
#
# Demonstrates the use of mmap to create a read-only memory-mapped file.
#
# Written by: David C. Morrill
# Date:       09/06/2002
# Copyright:  (c) 2002 by Enthought, Inc.
# License:    BSD Style.

#-- Imports --------------------------------------------------------------------

from __future__ import absolute_import, division, print_function, unicode_literals

if sys.version_info[0] < 3:
    import cPickle as pickle
else:
    import pickle

# For pickle file
import scipy.sparse as sps

#-- Globals --------------------------------------------------------------------

# Test file name:
filename = 'mmap_test.txt'
# Number of items to write to file:
nbytes = 100000
# Size of each item:
size = 1
# Type of each item:
type = 'b'
# The memory-mapped file object:
m = None

#-- Create the test file -------------------------------------------------------

# Open the test file for writing:
f = open

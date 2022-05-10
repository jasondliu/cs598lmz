import mmap
# Test mmap.mmap(-1, 1, mmap.ACCESS_READ)

import sys
# Test sys.__stdin__
# Test sys.__stdout__
# Test sys.__stderr__
# Test sys.__displayhook__
# Test sys.__excepthook__
# Test sys.__stderr__.write("x\n")
# Test sys.__stderr__.write("x\n")

import __builtin__
# Test __builtin__.sum((1,2,3), 0)
# Test __builtin__.sum((1,2,3), "")

# Test __builtin__.enumerate((1,2,3))
# Test __builtin__.enumerate((1,2,3), 2)

# Test __builtin__.map(lambda x: x, (1,2,3))
# Test __builtin__.map(lambda x,y: x+y, (1,2,3), (1,2,3))
# Test __builtin__.map(lambda x,y: x+

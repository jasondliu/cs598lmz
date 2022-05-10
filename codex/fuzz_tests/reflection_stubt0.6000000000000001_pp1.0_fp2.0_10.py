fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# should raise TypeError:
# __code__ must be a code object
"""

#__debug__ = True

import sys

#print(sys.__debug__)

#print(not sys.__debug__)

#print(sys.__debug__)

#print(not sys.__debug__)

"""
#__debug__ = True

import sys

print(sys.__debug__)

print(not sys.__debug__)

print(sys.__debug__)

print(not sys.__debug__)
"""

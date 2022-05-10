import types
types.add(types.IntType)

# This is a bit of an ugly hack, but we'll just put these
# warning filters in place and not tell the user about it.
# This should be OK because they're not usually going to be
# set by anyone but the user.
#
# Warnings aren't displayed by default since Python 2.6.  This
# code is necessary for earlier versions of Python.

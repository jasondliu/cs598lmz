import ctypes
# Test ctypes.CFUNCTYPE
#
# The following test fails on Windows XP 32-bit with Python 2.7.2
#
# The problem is that the function pointer is not properly aligned
# on the stack.
#
# The problem was introduced by the following commit:
#
# commit 0f2e2f8e1b8d8b7c3b3a3d8c9f9f9d7f7b0e0d7c
# Author: Christian Heimes <christian@python.org>
# Date:   Tue Feb 22 18:22:30 2011 +0100
#
#     Issue #11894: Fix alignment of function arguments on the stack.
#
#     The alignment of function arguments on the stack is platform
#     dependent. On Windows 64-bit the alignment is 16 bytes.
#
#     The patch adds a new helper function _ctypes_get_fielddesc() that
#     returns a tuple of (offset, size, alignment) for a given type.
#     The alignment is calculated from the type's alignment attribute
#     and the alignment of the previous field.
#
#     The patch also

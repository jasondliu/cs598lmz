import _struct
# Test _struct.Struct
from test import support
# Create dummy Struct class
import _testcapi
from _testcapi import INT_MAX, UINT_MAX, PY_SSIZE_T_MAX, PY_SSIZE_T_MIN, \
    SIZEOF_PYGC_HEAD

NULL_VALUE = 0

if PY_SSIZE_T_MAX == INT_MAX:
    NULL_VALUE = NULL_VALUE - PY_SSIZE_T_MAX - 1

if PY_SSIZE_T_MIN == INT_MIN:
    NULL_VALUE = NULL_VALUE + PY_SSIZE_T_MIN + 1

if support.have_unicode:
    NULL_VALUE = NULL_VALUE + ord('\u1234')

# Issue #19540: The ssize_t type is defined in Python's pyport.h as
# either 'long' or 'long long', depending on the platform.
#
# This test needs to be careful when using the sizeof() macro
# because, in C, the following two statements are not equivalent:
#
#    sizeof(sizeof

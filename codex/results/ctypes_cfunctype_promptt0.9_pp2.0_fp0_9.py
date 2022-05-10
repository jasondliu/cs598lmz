import ctypes
# Test ctypes.CFUNCTYPE
# sf_proto.cl

# stdlib
import os
import tempfile

# Testing
import nose
from nose.tools import eq_, ok_, raises
from pyop2.utils import as_tuple


# Type to test
ctyp = ctypes.CFUNCTYPE

# Type tags
tags = [
    # Basic types
    'char',
    'signed char',
    'unsigned char',
    'short',
    'unsigned short',
    'int',
    'unsigned int',
    'long',
    'unsigned long',
    'long long',
    'unsigned long long',
    'float',
    'double',
    'long double',
    'wchar_t',
    'size_t',
    # Special types
    'void',
    'struct float2',
    'struct double2',
    'struct float4',
    'struct double4',
    'struct float8',
    'struct double8',
    'struct double16',
    # Pointers
    'char *',
    'signed char *

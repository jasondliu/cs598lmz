import ctypes
# Test ctypes.CField declaration for final field
#
# This C code should compile and run ok as a test
#
# typedef struct {
# 	int x;
# 	int y;
# } S;
#
# typedef struct {
# 	int a;
# 	int b;
# 	S s;
# 	int c;
# 	int d;
# } T;

import _ctypes_test

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)
                ]

class T(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('s', S),
                ('c', ctypes.c_int),
                ('d', ctypes.c_int)
                ]

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c

import ctypes
# Test ctypes.CFUNCTYPE
#
# Create a function pointer type, and test assigning it to a function and vice versa.
#
# Usage: test_cfunctype.py

import _ctypes_test

@_ctypes_test.testcode
def call_int_func(func):
    return func(1)

@_ctypes_test.testcode
def call_double_func(func):
    return func(1.0)

@_ctypes_test.testcode
def call_void_func(func):
    func()

@_ctypes_test.testcode
def call_string_func(func):
    return func("string")

@_ctypes_test.testcode
def call_bstring_func(func):
    return func(b"bytestring")

@_ctypes_test.testcode
def call_struct_func(func):
    return func((1, 2, 3))

@_ctypes_test.testcode
def call_struct_by_pointer_func(func):
    return func((1, 2, 3))

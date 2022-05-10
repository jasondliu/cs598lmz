import ctypes
# Test ctypes.CField

# This should be a public type
class public_type(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int)]

# This should be a private type
class _private_type(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int)]

# This should be a public type
class public_type_with_private_field(ctypes.Structure):
    _fields_ = [("value", _private_type)]

# This should be a private type
class _private_type_with_public_field(ctypes.Structure):
    _fields_ = [("value", public_type)]

# This should be a public type
class public_type_with_private_field_and_private_type(ctypes.Structure):
    _fields_ = [("value", _private_type_with_public_field)]

# This should be a private type
class _private_type_with_public_field_and_public_type(ctypes.Structure):
    _fields_ = [

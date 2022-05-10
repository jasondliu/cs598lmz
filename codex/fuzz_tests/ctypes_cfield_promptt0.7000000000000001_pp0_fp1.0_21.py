import ctypes
# Test ctypes.CField macro
#
# To test:
#
#    gcc -c -O -Wall -Werror -fPIC test_cfield.c
#    gcc -shared -o test_cfield.so test_cfield.o
#    python test_cfield.py

ctypes.cdll.LoadLibrary("./test_cfield.so")

from ctypes import *

class Struct1(Structure):
    _fields_ = [
        ('a', c_int),
        ('b', c_int)]

class Struct2(Structure):
    _fields_ = [
        ('s2a', Struct1),
        ('s2b', Struct1)]

class Struct3(Structure):
    _fields_ = [
        ('s3a', Struct2),
        ('s3b', Struct2)]

class Struct4(Structure):
    _fields_ = [
        ('s4a', Struct3),
        ('s4b', Struct3)]

class Struct5(Structure):
    _fields_ = [
        ('s5a', Struct

import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.CField)]

class D(C):
    _fields_ = [
        ('d', ctypes.c_int),
        ('e', ctypes.c_int)]

class E(D):
    _fields_ = [
        ('f', ctypes.c_int),
        ('g', ctypes.c_int)]

class F(E):
    _fields_ = [
        ('h', ctypes.c_int),
        ('i', ctypes.c_int)]

class G(F):
    _fields_ = [
        ('j', ctypes.c_int),
        ('k', ctypes.c_int)]

class H(G):
    _fields_ = [
        ('l', ctypes.c_int),
        ('m', ctypes.c_int)]

class I(H):
    _fields_ = [

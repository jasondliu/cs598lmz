import _struct
import math
import random
import sys

#-------------------------------------------------------------------------------

def _magnitude(x, y, z):
    return math.sqrt(x * x + y * y + z * z)

#-------------------------------------------------------------------------------

def _normalize(x, y, z):
    m = _magnitude(x, y, z)
    if (m != 0):
        return (x / m, y / m, z / m)
    else:
        return (x, y, z)

#-------------------------------------------------------------------------------

def _rotate(x, y, z, rx, ry, rz):
    x, y, z = _normalize(x, y, z)
    rx, ry, rz = _normalize(rx, ry, rz)
    u, v, w = _normalize(y * rz - z * ry, z * rx - x * rz, x * ry - y * rx)

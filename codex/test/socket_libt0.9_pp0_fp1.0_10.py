import socket
import datetime


def d2b(b,n):
    l = '0'*n
    c = bin(b)[2:]
    for i in range(n-len(c)):
        c = '0' + c
    return l[:n-len(c)]+c


def d2b4(b):
    return d2b(b,4)


def d2b8(b):
    return d2b(b,8)


def d2b16(b):
    return d2b(b,16)


def d2b32(b):
    return d2b(b,32)


def b2d(b):
    return int(b, 2)


def b2d32(b):
    return b2d(b)


def b2d16(b):
    return b2d(b)


def b2d8(b):
    return b2d(b)


def b2d4(b):
    return b2d(b)



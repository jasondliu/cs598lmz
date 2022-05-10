import sys, threading
threading.Thread(target=lambda: sys.stdout.write('='), daemon=True).start()
import string, math, random, itertools, functools, operator
import struct, array, ctypes, collections

def read_int(): 
  return struct.unpack('I', f.read(4))[0]
def read_bytes(N): 
  return f.read(N)
def read_ints(N): 
  return struct.unpack('343I', f.read(N))

# input
f = open('input/D-large.in', 'rb')
T = read_int()

# output
o = open('output/output.out', 'wb')

# functions
def cross(v, w):
  return [v[1]*w[2] - v[2]*w[1], v[2]*w[0] - v[0]*w[2], v[0]*w[1] - v[1]*w[0]]

def sqlen(v):
  return v[0]*v[0] + v[1

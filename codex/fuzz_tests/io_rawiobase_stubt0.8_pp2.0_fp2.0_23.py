import io
class File(io.RawIOBase):
 def __init__(self,p):
  self.p = p
 def readinto(self,x):
  print(self.p,x)
  return x
f = File('/tmp/test')
print(f.read(7))

import platform
print(platform.uname())

import os
print(os.path.dirname(__file__))

import os
print(os.environ['PATH'].split(os.path.pathsep))

import os
print(os.getcwd())

def f():
 f()
f()

import os 
print(os.path.dirname('/home/python/a/b/c'))

import os
a = os.path.dirname('/home/python/a/b/c')
print(a)

def f():
 print ('a')
 f()
if __name__ == '__main__':
 f()

def f():
 print('a')
 f()
f()

def f():
 print('a')
 f()
f()



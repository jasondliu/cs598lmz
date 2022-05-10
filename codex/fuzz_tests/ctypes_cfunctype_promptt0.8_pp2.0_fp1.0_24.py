import ctypes
# Test ctypes.CFUNCTYPE
def hello(msg, repeat=1):
  print 'Hello %s' % msg * repeat
  return 1

myCallback = ctypes.CFUNCTYPE(
    ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int)(hello)

myCallback('a', 3)

def test(x, y, z=3):
  print x, y, z

test(4, 5, 6)

def test(*args, **kwargs):
  print(args, kwargs)

test(4, 5, 6, **{'x': 1, 'y': 2, 'z': 3})

def test(x, y, z=3, *args, **kwargs):
  print(x, y, z, args, kwargs)

test(4, 5, 6, **{'x': 1, 'y': 2, 'z': 3})
#!/usr/bin/env python
#coding:utf-8

#匿名函数
#lambda函数


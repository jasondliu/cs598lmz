import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return "hello"

def test_fun():
  assert fun() == "hello"

class TestClass:
  def __init__(self):
    self.fun = fun
  def test_fun(self):
    assert self.fun() == "hello"

def test_class():
  TestClass().test_fun()

if __name__ == '__main__':
  import sys
  import os
  import unittest
  if os.path.dirname(sys.argv[0]):
    os.chdir(os.path.dirname(sys.argv[0]))
  unittest.main()

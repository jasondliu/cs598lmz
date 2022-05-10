import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return 1

def f():
  fun()

f()
"""

def test_c_function_with_c_function_as_callback():
  run(C_FUNCTION_WITH_C_FUNCTION_AS_CALLBACK,
      expected_output='')


C_FUNCTION_WITH_C_FUNCTION_AS_CALLBACK_2 = """\
import ctypes

def f():
  print 'f'
  return 1

def g():
  print 'g'
  return 2

def h():
  print 'h'
  return 3

def i():
  print 'i'
  return 4

def j():
  print 'j'
  return 5

def k():
  print 'k'
  return 6

def l():
  print 'l'
  return 7

def m():
  print 'm'
  return 8

def n():
  print 'n'
  return 9

def o():
  print 'o'
  return 10

def p

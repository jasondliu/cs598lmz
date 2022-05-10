import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte
    y = ctypes.c_byte

s = S(3, 4)

def f():
    global s
    i = ctypes.c_byte(1)
    assert s.x == 3
    s.x = 2 
    assert s.x == 2
    assert i.value == 1
    i.value = 2 
    assert i.value == 2

f()
assert s.x == 2
"""

c_source_template = """
#include <Python.h>

// Type declarations

%(type_decls)s

// The module methods

%(method_defs)s

// Module initialization

PyMODINIT_FUNC
init%(module_name)s(void)
{
  PyObject* m;
  PyObject* d;
  PyObject* item;
  int i;
  int min_id = 0;
  int max_id = 0;
  
  m = Py_InitModule("%(module_name)s", %(module_name)s

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.pythonapi.Py_GetPythonDLL()
assert fun() != None, "Py_GetPythonDLL() returned None"

# Test Py_GetProgramName().
import sys
assert sys.executable == ctypes.pythonapi.Py_GetProgramName()

# Test Py_GetPath().
assert sys.path == ctypes.pythonapi.Py_GetPath(), 'Py_GetPath() returned  %r' % ctypes.pythonapi.Py_GetPath()

# Test Py_GetArgcArgv().
assert sys.argv == ctypes.pythonapi.Py_GetArgcArgv()[1], 'Py_GetArgcArgv() returned  %r' % ctypes.pythonapi.Py_GetArgcArgv()

# Test PyImport_GetModuleDict().
assert sys.modules == ctypes.pythonapi.PyImport_GetModuleDict()

# Test PyImport_AddModule().
mname = 'fakemodule'
assert not mname in sys.modules, '%s already exists in sys.modules' % global_name
fake

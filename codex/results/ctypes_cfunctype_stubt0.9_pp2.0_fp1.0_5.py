import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    a = 1
    return a

lib = ctypes.cdll.LoadLibrary('libpycmake.so')
lib.cmake_python_add_function.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.py_object, ctypes.py_object]
lib.cmake_python_add_function(ctypes.byref(fun.__dict__['_restype_']), fun, None)
</code>
In the CMakeLists.txt I try to call the function with python_call().
<code>cmake_python_add_function(fun)
python_call(fun 1)
</code>
When I run this I get an error similar to the previous one.
<code>CMake Error at test.cmake:21 (python_call):
  python_call encountered invalid arguments
  Policy CMP0045 is not set: Error if non-existent target_link_libraries
    libraries are passed to target_link_libraries.  Run "cmake
    --help-policy CMP0045" for policy details.

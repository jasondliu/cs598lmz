import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def test_c_function(func):
    # Run the function
    func()
    # Check the output
    assert np.allclose(c_func.x, np.ones(5))

def test_c_function_from_py_func(func):
    # Run the function
    func()
    # Check the output
    assert np.allclose(c_func.x, np.ones(5))

def test_c_function_from_py_func_with_c_func(func):
    # Run the function
    func()
    # Check the output
    assert np.allclose(c_func.x, np.ones(5))

def test_c_function_from_py_func_with_py_func(func):
    # Run the function
    func()
    # Check the output
    assert np.allclose(c_func.x, np.ones(5))

def test_c_function_from_py_func_with_py_func_and_c_func(func):


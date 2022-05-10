import ctypes
# Test ctypes.CFUNCTYPE
def test_global_func(value):
    return value * 3
ctypes.CFUNCTYPE(ctypes.c_int)(test_global_func)(2)

# Test ctypes.WINFUNCTYPE
def test_win_func(value):
    return value * 4
ctypes.WINFUNCTYPE(ctypes.c_int)(test_win_func)(3)

# test function pointer argument
def test_cb_func(cb1, cb2):
    return cb1(cb2(1))

def test_cb_inner_func(value):
    return value + 1

# test function pointer return
@ctypes.CFUNCTYPE(ctypes.c_int)
def test_ret_func(value):
    return value + 1

def test_ret_cb_func():
    return test_ret_func

print(test_cb_func(test_cb_func, test_cb_inner_func))
print(test_ret_cb_func()(3))


# test addressof function 


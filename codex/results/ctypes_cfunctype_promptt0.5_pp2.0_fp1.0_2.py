import ctypes
# Test ctypes.CFUNCTYPE
#
# Note: This test is currently disabled, because it crashes
# on Windows.
#
# @skip("win32")
# @needs_type_collector
# def test_CFUNCTYPE():
#     import _ctypes
#     def f(i):
#         return i+1
#     f.__name__ = 'f'
#     f.__module__ = 'test_CFUNCTYPE'
#     tp = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
#     #
#     p = tp(f)
#     assert p(1) == 2
#     #
#     p = tp(lambda i: i+1)
#     assert p(1) == 2
#     #
#     p = tp(ctypes.c_int.from_address(id(f)))
#     assert p(1) == 2
#     #
#     p = tp(ctypes.c_int.from_address(id(lambda i: i+1)))
#

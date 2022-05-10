gi = (i for i in ())
# Test gi.gi_code is None but gi.gi_frame is not None
if gi.gi_code is None and gi.gi_frame is not None:
    raise RuntimeError("This should never happen")

import _testcapi

def test_is_true(msg, x):
    if not x:
        raise Exception(msg)

_testcapi.test_exception_getter_setter_exc.__doc__ = (
    "Raise an exception that has a docstring, "
    "then return its __getitem__ and __setitem__ methods.")

_testcapi.test_exception_getter_setter_obj.__doc__ = (
    "Raise an exception that has a docstring, "
    "then return its __getitem__ and __setitem__ methods.")

try:
    __getitem__, __setitem__ = _testcapi.test_exception_getter_setter_exc()
    test_is_true("exception __getitem__ method is not callable",
                 callable(__getitem__))
   

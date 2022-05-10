fn = lambda: None
# Test fn.__code__: implemented by a code object (co_code)
test_fn.__code__ = types.CodeType(
    0, 0, 0, 0, b"c" * 32, tuple(), tuple(),
    tuple(), tuple(), b"dummy", b"dummy.py", 1,
    b"dummy_function", 0, 0)
# Ensure that test_fn can be executed (e.g., is callable)
test_fn.__code__.co_code = b"\x64\x00\x00\x00\x00\x00\x00\x00"
test_fn.__code__.co_consts = (None, )
# Test fn.__globals__: implemented by a dictionary mapping global names to
# their values
test_fn.__globals__ = {"a": 1}
# Test fn.__closure__: implemented by a tuple of cells containing variables
# closed over by this function
cell = test_fn.__closure__ = (None, )
# Test cell.cell_contents: implemented by the value contained in this cell
cell[

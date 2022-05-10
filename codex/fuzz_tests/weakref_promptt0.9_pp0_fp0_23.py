import weakref
# Test weakref.ref by trying to extract a file name from an open file.
# The file object is passed to a function that stores a circular reference
# to it.
import io
def let_file_be_released(f):
    f.some_data = f
    wr = weakref.ref(f)
    return wr
with open(__file__) as f:
    wr = let_file_be_released(f)
    f = None
    assert wr() is None

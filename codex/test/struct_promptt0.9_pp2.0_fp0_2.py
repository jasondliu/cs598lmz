import _struct
# Test _struct.Struct().buffer_info()

import array
import sys

class SmallShortArray(array.array):
    """Just long enough to check the low-level ops"""
    itemsize = 2

def test(st, buf):

    # Find a large buffer, to avoid possible problems
    # at small buffer sizes.
    for size in xrange(1, 10000):
        try:
            x = st.buffer_info(buf)
        except BufferError:
            continue
        else:
            if x[1] == st.size:
                break
            else:
                raise Exception("buffer size (%d) != struct size (%d)" %
                                (x[1], st.size))
    else:
        raise Exception("Unable to create a large enough buffer")

    # Check that the right buffer is returned
    return x[0] is buf



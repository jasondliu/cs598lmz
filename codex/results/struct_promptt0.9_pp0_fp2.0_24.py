import _struct
# Test _struct.Struct() and .pack() / .unpack()

structu64 = _struct.Struct("u64")

def test_u64():
    for val in [0, 27, 32, 1000, 127<<10, 127<<20, 127<<30,
                (1<<31) - 1, 1<<31, 1<<35, (1<<61)-1]:
        val = val<<3
        p = structu64.pack(val)
        assert structu64.unpack(p) == (val,)


def test_u64_overflow():
    py.test.raises(struct.error, structu64.pack, -1)
    py.test.raises(struct.error, structu64.pack, 1<<64)
    py.test.raises(struct.error, structu64.pack, 1<<128)

# Test signed ints

structs64 = _struct.Struct("s64")

def test_s64():
    for val in [-((1<<61)-1), -(1<<61), -(1<<60), -(1<<31

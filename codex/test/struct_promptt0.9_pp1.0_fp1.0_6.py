import _struct
# Test _struct.Struct


def test_struct_module():
    import _struct as _struct

    def do_test(fmt, sz, val, res=None):
        if sz > 8:
            py.test.skip("not yet supported packing float >64 bits")
        if res is None:
            res = val
        s = _struct.Struct(fmt)
        # Test packing
        expected = _struct.pack(fmt, val)
        got = s.pack(val)
        assert expected == got

        # Test unpacking
        expected = _struct.unpack(fmt, got)
        got = s.unpack(got)
        assert expected == got

        # Test iteration
        expected = list(iter(_struct.iter_unpack(fmt, got)))
        got = list(iter(s.iter_unpack(got)))
        assert expected == got

    # Integers
    do_test("@B", 1, 42)
    do_test("@b", 1, -42)
    do_test("@H", 2, 42)
    do_test

from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda: 8
s.pack = lambda x: b"\x00"*8
s.unpack = lambda x: (x, "")
s.unpack_from = lambda x, y: (x, "")
s.iter_unpack = lambda x: [x for i in range(8)]
s.format = "=8s"
s.format_size = lambda: 8
s.format_parser = lambda x: (8, "<8s")

@pytest.mark.parametrize("s", [Struct(b"=Q"), s])
def test_Buffer_from_memoryview(s):
    b = Buffer(memoryview(b"\x00"*8), s)
    assert b.order == b.native_order
    assert b.itemsize == s.size()
    assert b.view(s) is None
    assert b.format == s.format
    assert b.shape == (8,)
    assert b.ndim == 1
    assert b.strides == (8,)
    assert b.size == 8


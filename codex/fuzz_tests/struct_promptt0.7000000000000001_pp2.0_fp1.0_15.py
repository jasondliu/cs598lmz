import _struct
# Test _struct.Struct
def test_struct():
    _struct.Struct("i").pack(0x12345678)

# Test _struct.unpack_from
def test_unpack_from():
    import array
    data = array.array("b", [0x12, 0x34, 0x56, 0x78])
    _struct.unpack_from("i", data, 0)

def test_pyc_magic():
    import imp
    imp.get_magic()

# Test _imp.extension_suffixes
def test_ext_suffixes():
    import _imp
    _imp.extension_suffixes()

def test_unicode_file():
    import codecs, io
    f = codecs.open(__file__, "r", "utf-8")
    b = f.read()
    f2 = io.BytesIO(b.encode("utf-8"))
    f2.read()
    f2.seek(0)
    f2.read()

def test_long_to_float():
    a = 4

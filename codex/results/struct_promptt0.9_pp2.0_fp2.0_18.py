import _struct
# Test _struct.Struct

def _try_format (format):
    size = struct.calcsize(format)
    struct._Struct(format)
    S = struct.Struct(format)
    try:
        S.unpack_from("x" * size)
    except struct.error:
        pass
    S.pack(*range(1, size + 1))
    assert S.size == size
    try:
        S.pack("x" * size)
    except struct.error:
        pass
    try:
        S.pack(*range(size + 1))
    except struct.error:
        pass


class FormatTest(unittest.TestCase):
    def test_creation(self):
        # Test the success cases:
        for f in ("@", "h", "<h", ">h", "!", "4h", "4b", "4b4h", "8s",
                  "f", "d", "bcd", "=h", "!h", ">f"):
            try:
                struct._Struct(f)
                struct.Struct(f)
           

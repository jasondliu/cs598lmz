import _struct
# Test _struct.Struct

def test_struct_error(self):
    # Check that the right exception is raised for each error
    def struct_error(fmt):
        try:
            _struct.Struct(fmt)
        except _struct.error as msg:
            return msg
        else:
            raise RuntimeError("_struct.error not raised")

    self.assertEqual(struct_error(""), "empty format string")
    self.assertEqual(struct_error("P"), "bad char in format string: 'P'")
    self.assertEqual(struct_error("i\x00"), "bad char in format string: '\\x00'")
    self.assertEqual(struct_error("iP"), "bad char in format string: 'P'")
    self.assertEqual(struct_error("iiP"), "bad char in format string: 'P'")
    self.assertEqual(struct_error("Pii"), "bad char in format string: 'P'")
    self.assertEqual(struct_error("4P"), "bad char in format string: 'P'")

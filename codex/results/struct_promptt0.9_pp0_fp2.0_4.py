import _struct
# Test _struct.Struct against struct.Struct.

# TODO(benh): This is pretty lame and doesn't actually test anything.

PICKLES = ["banana", "corn is yummy", "green eggs and ham"]

test_data = [
  (0xFF,            "B"),
  (0xFF,            "b"),
  (0xFF,            "H"),
  (0xFF,            "h"),
  (0xFFFFFF,        "I"),
  (0xFFFFFF,        "i"),
  (0xFFFFFFFF,      "L"),
  (0xFFFFFFFF,      "l"),
  (0xFFFFFFFFFF,    "Q"),
  (0xFFFFFFFFFF,    "q"),
  (0.42,            "f"),
  (0.42,            "d"),
  (struct,          "i"),
  (PICKLES,         "i"),
  ("banana",        "4s"),
  ]

class StructCompatibilityTestCase(unittest.TestCase):
  def test_pack(self):
    print

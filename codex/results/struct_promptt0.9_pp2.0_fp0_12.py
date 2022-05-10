import _struct
# Test _struct.Struct.
struct = _struct.Struct("LLLL")
print struct.format # struct.format is treated as a variable up until it gets computed by struct.pack
print struct.size

# A struct used for this test
class Struct2(object):
    def x(value):
        return 42 << value

struct = Struct2()

# Test parser.
parser = _struct.Parser()
parser.add_option("--foo", default=struct.x(7), type="int", dest="foo", help="foo")
parser.add_options(foo=42)
print parser.get_default("foo", type="int")
# Create a new parser by extending an old one.
parser = parser.extend({"foo": 42})
print parser.__doc__
parser.print_help()
print parser.values.foo

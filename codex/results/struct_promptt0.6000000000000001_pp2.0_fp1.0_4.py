import _struct
# Test _struct.Struct.__new__ with a number of different types of
# arguments.

# This is equivalent to the C structure:
#     struct foo {char a; short b; int c; long long d;};
fmt = _struct.Struct('cbq')

# This is equivalent to the C structure:
#     struct bar {int a; double b;};
fmt2 = _struct.Struct('id')

# This is equivalent to the C structure:
#     struct foobar {char a; short b; int c; long long d; int e; double f;};
fmt3 = _struct.Struct('cbqid')

# This is equivalent to the C structure:
#     struct baz {char a; double b;};
fmt4 = _struct.Struct('cd')

# This is equivalent to the C structure:
#     struct quux {int a; char b;};
fmt5 = _struct.Struct('ic')

# This is equivalent to the C structure:
#     struct fred {char a; char b;};
fmt6 = _struct.Struct('cc

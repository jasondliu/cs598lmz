import _struct
# Test _struct.Struct
st = _struct.Struct("abcd")
# §py.test -s --pdb test_struct.py
# Convert the format string to a Struct object
# $py.test -s --pdb test_struct.py::Test::test_struct
# Create a Struct object (fmt = "abcd"  big endian).
# $py.test -s --pdb test_struct.py::Test::test_struct::test_format
# The format string is a list of characters that specify the type of the fields.
# $py.test -s --pdb test_struct.py::Test::test_pack
# Provide the values for the Struct fields as arguments.
# $py.test -s --pdb test_struct.py::Test::test_pack_into
# $py.test -s --pdb test_struct.py::Test::test_pack_into_bad_buffer
# $py.test -s --pdb test_struct.py::Test::test_unpack
# $py.test -s --pdb test_struct.py::Test::test_unpack_from

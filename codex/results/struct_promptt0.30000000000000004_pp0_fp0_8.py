import _struct
# Test _struct.Struct

# Test _struct.Struct

import _struct

class TestStruct:

    def test_struct_doc(self):
        assert _struct.Struct.__doc__ == 'Compile and return a Struct object which writes and reads binary data according to the format string format.\n\nThe format string consists of one or more multibyte characters.  Each\ncharacter specifies an operation to be performed, and may be followed by\na count and additional arguments.  The following characters are\ncurrently defined:\n\n  @:  pad byte (no data);\n  x:  pad byte (no data);\n  c:  char;\n  b:  signed char;\n  B:  unsigned char;\n  ?:  _Bool (requires C99; if not available, char is used instead);\n  h:  short;\n  H:  unsigned short;\n  i:  int;\n  I:  unsigned int;\n  l:  long;\n  L:  unsigned long;\n  q:  long long;\n  Q: 

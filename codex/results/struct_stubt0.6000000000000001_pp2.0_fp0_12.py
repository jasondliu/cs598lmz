from _struct import Struct
s = Struct.__new__(Struct)
print(s)
s.format = 'I 2s f'
print(s)
s.size = s.calcsize(s.format)
print(s)

# _struct.Struct.__new__(format)
#   -> a new struct object which writes and reads binary data according to the format string format.
#   The format string is composed of format units.
#   Each format unit is a single character indicating a basic type,
#   or a repeat count followed by a format unit indicating a compound type.
#   The repeat count may be given as an integer or as '*' to denote a repeat count of the size of the argument list.
#   The following format units are defined.
#     'x'     pad byte (no data);
#     'c'     char;
#     'b'     signed char;
#     'B'     unsigned char;
#     '?'     _Bool;
#     'h'     short;
#     'H'     unsigned short;
#     'i'     int;
#     'I'     unsigned int;
#     'l

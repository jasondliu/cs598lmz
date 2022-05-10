from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# struct.Struct.__new__(format)
# Return a new Struct object which writes and reads binary data according to the format string format.
# The format string is composed of zero or more directives:
#     ordinary characters (not %), which are copied unchanged to the output
#     conversion specifications, each of which results in fetching zero or more arguments from the next position in the argument tuple.
#     The arguments are inserted into the output in place of the conversion specification.
#     The conversion specification starts with a % character.
#     After the %, the following appear in sequence:
#         Zero or more of the following flags:
#             #       An 'x' character in the flag field will cause a '0x' prefix to be added to the output value for %x conversions.
#                     The '0X' prefix is used for %X conversions.
#             0       The conversion will be zero padded for numeric values.
#             -       The converted value is left adjusted (overrides the '0'

from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(1)

# _struct.Struct.__new__(format, /, *args, **kwargs)
# Return a new Struct object which writes and reads binary data according to the format string format.
# The format string is composed of one or more of the following codes (in order):
#
# Format  C Type             Python type         Standard size
# ---------------------------------------------------------------------------------
#   x     pad byte           no value
#
#   c     char               string of length 1  1
#   b     signed char        integer             1
#   B     unsigned char      integer             1
#   ?     _Bool              bool                1
#
#   h     short              integer             2
#   H     unsigned short     integer             2
#
#   i     int                integer             4
#   I     unsigned int       integer             4
#
#   l     long               integer             4
#   L     unsigned long      integer             4
#   q     long long          integer             8
#   Q     unsigned long long integer             8
#


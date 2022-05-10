import _struct
# Test _struct.Struct.

# This is a test of the _struct module.
#
# The _struct module supports packing and unpacking of Python values
# using format strings similar to those used by the pack and unpack
# functions in the struct module.  The following format characters are
# supported:
#
# Format  C Type             Python type         Standard size
# x       pad byte           no value
# c       char               string of length 1
# b       signed char        integer
# B       unsigned char      integer
# h       short              integer
# H       unsigned short     integer
# i       int                integer
# I       unsigned int       integer
# l       long               integer
# L       unsigned long      integer
# f       float              float
# d       double             float
# s       char[]             string
# p       char[]             string
# P       void *             integer
#
# Compiled Struct objects support the following methods:
#
# pack(v1, v2, ...) -> string
#     Return a string containing the values v1, v2, ... packed according
#     to the format string.
#
# pack_

import _struct
# Test _struct.Struct and _struct.calcsize()
# However, the size of a C struct does not match the size of the corresponding
# Python struct for some packing combinations.  In particular, the following
# values do not match:

# 1-bit fields
# 1 or 2-byte character fields, plus length padding
# native packing of a structure containing only bit fields

# 1-bit fields
# This is a known problem.  Python structs have no 1-bit fields.
# 1 or 2-byte character fields, plus length padding
# 1 character fields are explicitly stated to be treated as 2-byte fields:

# 1-byte character fields are not supported, because ANSI/C does not
# specify how to handle them.  Use i:1 instead.

# The length padding occurs because the physical location of the field requires
# the structure to be length padded.  For example:

# struct foo {    
#     short s;    
#     char c;    
# };

# Here 'c' will be 2-bytes in physical memory.  Struct members are aligned to
# their natural alignment and a 2-byte character field would

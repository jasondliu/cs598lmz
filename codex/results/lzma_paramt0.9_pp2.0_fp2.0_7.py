from lzma import LZMADecompressor
LZMADecompressor().decompress(b"data with lzma compression")

# setValue
# Translate a single encoded integer value into the value
# for the Python interpreter.  Implemented as
# PyLong_FromLong for integer types, PyUnicode_FromString for
# string types, and long() for other types.
def setValue(obj, value):
    if obj.type == T_INTEGER:
        return int(value)
    elif obj.type == T_STRING:
        return str(value)
    else:
        return value

# walk
# Translate UTF8 into a Python Unicode string, possibly with debugging message.
def walk(utf8, indent=1):
    if debug_flag:
        print((indent*"    "+"walk 

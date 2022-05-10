import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

def print_unicode_list(seq):
    print(list(map(lambda x: '{:#04x}'.format(x) , seq)))

# TODO(iceboy): use better pybind11 types to avoid lots of extern "C"
c_wchar_p = ctypes.POINTER(ctypes.c_int16)
c_char_p = ctypes.POINTER(ctypes.c_byte)
class c_Py_ssize_t_CTypes(ctypes.c_ssize_t):
    def __init__(self, value):
        if isinstance(value, int):
            value = ctypes.c_ssize_t(value)
        super().__init__(value)

# strip BOM if exists
def codecs_unescape_encode(input_bytes, errors="strict", **options):
    result = codecs.escape_encode(input_bytes, errors=errors, **options)
    if result[0].startswith(b'\\x'):
        return (bytes([int(result[

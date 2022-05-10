import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

@parametrize.expand(itertools.product([bytes, unicode], ["%s", "%p"]))
@parametrize.enable_type_errors
def test_format_cfield(text_formatter, format_string):
    assert text_formatter(format_string, S.x) == text_formatter(format_string, id(S.x))

@parametrize.expand([
    (ctypes.create_string_buffer(b"\0"), "%s"),
    (ctypes.c_char_p(b"\0"), "%s"),
    (ctypes.c_char(b"\0"), "%s")
])
@parametrize.enable_type_errors
def test_format_c_string(c_string, format_string):
    assert text_formatter(format_string, c_string) == text_formatter(format_string, repr(c_string))

def test_error_message_on_formatter_not_being_a_string():
    error = pytest.ra

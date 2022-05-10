import _struct
# Test _struct.Struct() in both modes

def test_format_char():
    for fmt in (b'', b'@', b'=', b'<', b'>', b'!', b'&'):
        yield check_format_char, fmt
        yield check_format_char, fmt + b'8s'
        yield check_format_char, fmt + b'8s8s'

def check_format_char(fmt):
    s = _struct.Struct(fmt)
    assert s.format[0] in b'@=<>!&'

def test_unpack():
    for fmt in (b'', b'@', b'=', b'<', b'>', b'!', b'&'):
        yield check_unpack, fmt
        yield check_unpack, fmt + b'8s'
        yield check_unpack, fmt + b'8s8s'

def check_unpack(fmt):
    s = _struct.Struct(fmt)
    s.unpack(b'xxxx' + fmt)


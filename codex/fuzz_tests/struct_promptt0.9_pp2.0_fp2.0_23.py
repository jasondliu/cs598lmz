import _struct
# Test _struct.Struct() instance with multi-character format string.
_fmt_test = [
    ('hhi', -3, -3, -3),
    ('l5sb7shb', 4, 'hello', 'world!', -16, 35),
]
for fmt, *vals in _fmt_test:
    _fmt_obj = _struct.Struct(fmt)
    _len = _fmt_obj.size
    _bytes = _fmt_obj.pack(*vals)
    _unpack = _fmt_obj.unpack(_bytes)
    print(fmt, _len, _bytes, vals, _unpack)
    assert _bytes == _fmt_obj.pack(*vals)
    assert _unpack == vals

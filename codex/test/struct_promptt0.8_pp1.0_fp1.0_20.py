import _struct
# Test _struct.Struct objects with standard code argument
values = (1, 2.0, 3.0+0.0j)
for code in 'cbBhHiIlLfd':
    format = '<' + code
    x = _struct.Struct(format)
    s = x.pack(*values)
    y = _struct.Struct(format)
    z = y.unpack(s)

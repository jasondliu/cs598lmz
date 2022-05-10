import _struct
# Test _struct.Struct.__ne__()
for code in 'xcbhiIlLfdspP':
    format = code * 4
    s = _struct.Struct(format)
    if s != s:
        print(code, '-> not equal')

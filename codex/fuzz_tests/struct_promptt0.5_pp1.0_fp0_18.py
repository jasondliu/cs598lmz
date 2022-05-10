import _struct
# Test _struct.Struct.format_size()

s = _struct.Struct('hi')
s.format_size('<')
s.format_size('>')
s.format_size('@')

try:
    s.format_size('!')
except ValueError:
    pass
else:
    raise Exception("Didn't raise ValueError")

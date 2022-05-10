import _struct
# Test _struct.Struct.format_size()
for fmt in 'cbhilfdsp':
    _struct.Struct(fmt).format_size('=')
for fmt in 'BHILFDSP':
    _struct.Struct(fmt).format_size('=')
_struct.Struct('cc').format_size('=')
_struct.Struct('hh').format_size('=')
_struct.Struct('ii').format_size('=')
_struct.Struct('ll').format_size('=')
_struct.Struct('qq').format_size('=')
_struct.Struct('ff').format_size('=')
_struct.Struct('dd').format_size('=')
_struct.Struct('ss').format_size('=')
_struct.Struct('pp').format_size('=')
# Test _struct.Struct.__new__()
for fmt in 'cbhilfdsp':
    _struct.Struct(fmt)
for fmt in 'BHILFDSP':
    _struct.Struct(fmt)
_struct.Struct('cc')
_struct.Struct('hh')


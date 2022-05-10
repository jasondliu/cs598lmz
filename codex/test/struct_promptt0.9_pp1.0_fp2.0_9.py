import _struct
# Test _struct.Struct.build_params() function
_struct.Struct.build_params(('5s', '4L', '@4f', '10d', '4h')) == {
    'endian': '@', 'fmt': ('s', '>L', 'f', 'd', 'h')}
_struct.Struct.build_params(('!s', '<L')) == {
    'endian': '', 'fmt': ('s', '<L')}
_struct.Struct.build_params(('<s', '!L')) == {
    'endian': '<', 'fmt': ('s', 'L')}
_struct.Struct.build_params(('@L', '<f')) == {
    'endian': '<', 'fmt': ('L', 'f')}
_struct.Struct.build_params('bhl') == {
    'endian': '@', 'fmt': ('b', 'h', 'l')}

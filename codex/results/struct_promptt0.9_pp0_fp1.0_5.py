import _struct
# Test _struct.Struct.unpack_from() method.

import _struct

PACKET_DATA = [
    b'abcabcabcabcabcabcabcabcabcabcabcabcabca',
    b'0123456789012345012345678901234501234567',
    b'defdefdefdefdefdefdefdefdefdefdefdefdefdef',
    b'0123456789012345012345678901234501234567',
    b'abcabcabcabcabcabcabcabcabcabcabcabcabca',
    b'0123456789012345012345678901234501234567',
    b'defdefdefdefdefdefdefdefdefdefdefdefdefdef',
    b'0123456789012345012345678901234501234567',
    b'abcabcabcabcabcabcabcabcabcabcabcabcabca',
    b'0123456789012345012345678901234501234567',
    b'defdefdefdefdefdefdefdefdefdef

import _struct
# Test _struct.Struct

import struct

def check_sizeof(fmt):
    s = struct.Struct(fmt)
    return s.size

def test_sizeof():
    assert check_sizeof('x') == 1
    assert check_sizeof('c') == 1
    assert check_sizeof('b') == 1
    assert check_sizeof('B') == 1
    assert check_sizeof('?') == 1
    assert check_sizeof('h') == 2
    assert check_sizeof('H') == 2
    assert check_sizeof('i') == 4
    assert check_sizeof('I') == 4
    assert check_sizeof('l') == 4
    assert check_sizeof('L') == 4
    assert check_sizeof('q') == 8
    assert check_sizeof('Q') == 8
    assert check_sizeof('f') == 4
    assert check_sizeof('d') == 8
    assert check_sizeof('s') == 1
    assert check_sizeof('p') == 1
    assert check_sizeof('P') == 4

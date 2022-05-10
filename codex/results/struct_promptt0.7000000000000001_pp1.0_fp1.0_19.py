import _struct
# Test _struct.Struct

def get_size(typestr):
    try:
        return _struct.calcsize(typestr)
    except Exception as e:
        return e

def test_struct_format():
    assert get_size('=') == 0
    assert get_size('=B') == 1
    assert get_size('=b') == 1
    assert get_size('=H') == 2
    assert get_size('=h') == 2
    assert get_size('=I') == 4
    assert get_size('=i') == 4
    assert get_size('=L') == 4
    assert get_size('=l') == 4
    assert get_size('=Q') == 8
    assert get_size('=q') == 8
    assert get_size('=P') == 8
    assert get_size('=f') == 4
    assert get_size('=d') == 8
    assert get_size('=s') == 'must have exact number of items for pack'
    assert get_size('=p') == 'must have exact number of items for

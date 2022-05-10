import _struct
# Test _struct.Struct.format

def test_format():
    # Test the format method of Struct
    S = _struct.Struct
    assert S('i').format == 'i'
    assert S('ii').format == 'ii'
    assert S('iih').format == 'iih'
    assert S('iih9s').format == 'iih9s'
    assert S('iih9sP').format == 'iih9sP'
    assert S('=i').format == '=i'
    assert S('=ii').format == '=ii'
    assert S('=iih').format == '=iih'
    assert S('=iih9s').format == '=iih9s'
    assert S('=iih9sP').format == '=iih9sP'
    assert S('@i').format == '@i'
    assert S('@ii').format == '@ii'
    assert S('@iih').format == '@iih'
    assert S('@iih9s').format == '@iih9s'
    assert S

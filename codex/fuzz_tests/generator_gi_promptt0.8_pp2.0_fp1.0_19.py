gi = (i for i in ())
# Test gi.gi_code not being reset


def check_mutable_code(m):
    assert m.__code__.co_filename == __file__
    assert m.__code__.co_firstlineno == m.__code__.co_lnotab[:2]
    assert m.__code__.co_firstlineno == 2
    assert m.__code__.co_lnotab[:2] == 2
    assert m.__code__.co_lnotab[2:] == b'\x01\x01'
    return m()


def check_immutable_code(m):
    assert m.__code__.co_filename == __file__
    assert m.__code__.co_firstlineno == m.__code__.co_lnotab[:2]
    assert m.__code__.co_firstlineno == 5
    assert m.__code__.co_lnotab[:2] == 5
    assert m.__code__.co_lnotab[2:] == b'\x01\x01'
    return m()

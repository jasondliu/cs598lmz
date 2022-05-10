gi = (i for i in ())
# Test gi.gi_code
gi = (i for i in ())
# Test gi.gi_frame
gi = (i for i in ())
# Test gi.gi_running
# Test gi.gi_yieldfrom


# GENERATOR EXTENDED UNPACKING

def test_tuple_assign_to_tuple():
    """Assigning to a tuple of targets"""
    (a, b, c) = (1, 2, 3)
    assert a == 1
    assert b == 2
    assert c == 3

def test_tuple_assign_to_list():
    """Assigning to a list of targets"""
    [a, b, c] = (1, 2, 3)
    assert a == 1
    assert b == 2
    assert c == 3

def test_tuple_assign_to_mixed_list():
    """Assigning to a list of targets"""
    [a, b, c] = (1, 2, [4, 5])
    assert a == 1
    assert b == 2
    assert c[0] == 4
    assert

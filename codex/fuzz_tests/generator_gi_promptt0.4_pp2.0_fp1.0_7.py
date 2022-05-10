gi = (i for i in ())
# Test gi.gi_code is not None

# Test __length_hint__
def test_length_hint():
    assert [].__length_hint__() == 0
    assert [1].__length_hint__() == 1
    assert [1, 2].__length_hint__() == 2
    assert [1, 2, 3].__length_hint__() == 3
    assert [1, 2, 3, 4].__length_hint__() == 4
    assert [1, 2, 3, 4, 5].__length_hint__() == 5
    assert [1, 2, 3, 4, 5, 6].__length_hint__() == 6
    assert [1, 2, 3, 4, 5, 6, 7].__length_hint__() == 7
    assert [1, 2, 3, 4, 5, 6, 7, 8].__length_hint__() == 8
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9].__length_hint__() == 9
    assert [1, 2, 3, 4,

fn = lambda: None
gi = (i for i in ())
fn.__code__ = None

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert remove_all_before(gi, 1) == [1, 2, 3]
    assert remove_all_before(gi, -1) == []
    assert remove_all_before(fn, 1) == []
    assert remove_all_before([0, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 4], 0) == [1, 0, 0, 2, 0, 0, 3, 0, 0, 4]
    assert remove_all_before([0, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 4], -1) == []
    assert remove_all_before([1, 2, 3], 1) == [1, 2, 3]
    assert remove_all_before([1, 2, 3], 2) == [2, 3]
    assert remove_all_before([1, 2, 3], 3) == [3]


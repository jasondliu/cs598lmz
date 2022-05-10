import selected
 
def test_transpose_zip():
    assert selected.transpose([[1, 2, 3], [4, 5, 6]]) == [(1, 4), (2, 5), (3, 6)]
 
def test_transpose_none():
    assert selected.transpose([[1, 2], [3, 4], [5, 6], [7, 8]]) == [(1, 3, 5, 7), (2, 4, 6, 8)]
 
def test_transpose_gzip():
    assert selected.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
 
def test_transpose_error():
    assert selected.transpose([[1, 2, 3], [4, 5]]) == "Up to you"

def test_flatten_ok():
    assert selected.flatten([1, 2, [3, 4, [5]]]) == [1, 2, 3, 4, 5]


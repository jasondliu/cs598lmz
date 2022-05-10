import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

@pytest.mark.parametrize("value, expected", [
    (1, 1),
    (-1, -1),
    (1.0, 1),
    (True, 1),
    (False, 0),
    ("1", 1),
    ([1], ValueError()),
    ({1}, ValueError()),
    (S, AttributeError()),
    (S(1), 1),
    (S(x=2) , 2),
    (S(x=S(1)), 1),
    (S(1).x, 1),
    (S(x=S(1)).x, 1),
])
def test_coercion(value, expected):
    if isinstance(expected, type):
        with pytest.raises(expected):
         

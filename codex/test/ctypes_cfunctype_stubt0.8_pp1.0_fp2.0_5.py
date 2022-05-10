import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return type(None)

def test_import_numpy_as_np():
    import numpy as np
    assert np.__name__ == "numpy"
    assert np.sqrt(4) == 2.0

def test_import_numpy_as_np_and_math_as_m():
    import math as m
    import numpy as np
    assert m.__name__ == "math"
    assert np.__name__ == "numpy"
    assert m.sqrt(4) == 2.0
    assert np.sqrt(4) == 2.0

def test_import_numpy_in_a_list():
    import numpy, math
    assert numpy.__name__ == "numpy"
    assert math.__name__ == "math"
    assert numpy.sqrt(4) == 2.0
    assert math.sqrt(4) == 2.0

def test_import_numpy_directly():
    import numpy
    assert numpy.__name__ == "numpy"

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5

def get_pyscript():
    return pytest.approx(5)

def get_pyscript_list():
    return [pytest.approx(5)]

def get_pyscript_matrix():
    return [[pytest.approx(5)]]

def get_pyscript_cplx():
    return pytest.approx(5 + 3j)

def get_pyscript_cplx_list():
    return [pytest.approx(5 + 3j)]

def get_pyscript_cplx_matrix():
    return [[pytest.approx(5 + 3j)]]


def get_pyscript_dict():
    return {'a': pytest.approx(5)}

def get_pyscript_list_dict():
    return [{'a': pytest.approx(5)}]

def get_pyscript_dict_list():
    return {'a': [pytest.approx(5)]}


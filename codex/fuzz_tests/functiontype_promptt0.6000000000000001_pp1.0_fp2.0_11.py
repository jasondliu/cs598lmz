import types
# Test types.FunctionType

def test_function_type_1():
    def func(): pass

    assert isinstance(func, types.FunctionType)


def test_function_type_2():
    def func(x): pass

    assert isinstance(func, types.FunctionType)


def test_function_type_3():
    def func(x, y): pass

    assert isinstance(func, types.FunctionType)


def test_function_type_4():
    def func(**x): pass

    assert isinstance(func, types.FunctionType)


def test_function_type_5():
    def func(**x): pass

    assert isinstance(func, types.FunctionType)


def test_function_type_6():
    def func(x, **y): pass

    assert isinstance(func, types.FunctionType)


def test_function_type_7():
    def func(x, *y): pass

    assert isinstance(func, types.FunctionType)


def test_function_type_8():
    def func(x, *y, **z

import types
# Test types.FunctionType()...
def test_function_type_1():
    def foo():
        pass
    assert isinstance(foo, types.FunctionType)
# Test eval()...
def test_eval_1():
    eval('1')
# Test apply()...
def test_apply_1():
    def foo(x):
        return x
    assert apply(foo, (1,)) == 1
# Test map()...
def test_map_1():
    def foo(x):
        return x
    assert map(foo, [1]) == [1]
# Test filter()...
def test_filter_1():
    def foo(x):
        return x
    assert filter(foo, [1]) == [1]
# Test reduce()...
def test_reduce_1():
    def foo(x, y):
        return x + y
    assert reduce(foo, [1]) == 1
# Test zip()...
def test_zip_1():
    assert zip([1], [1]) == [(1, 1)]
# Test hasattr()...
def test_hasattr_

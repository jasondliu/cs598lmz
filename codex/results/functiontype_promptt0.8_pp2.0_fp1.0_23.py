import types
# Test types.FunctionType(..., **kwds)

def tf(x):
    "Dummy function."
    return x

def test_function_type_keyword():
    with pytest.raises(TypeError):
        types.FunctionType(tf.__code__, globals(), 'foo')

def test_function_type_starargs():
    assert tf.__code__.co_flags & CO_VARARGS
    assert tf.__code__.co_flags & CO_VARKEYWORDS
    with pytest.raises(TypeError):
        types.FunctionType(tf.__code__, globals(), 'foo', (), ())

def test_function_type_kwargs():
    with pytest.raises(TypeError):
        types.FunctionType(tf.__code__, globals(), 'foo', (), {})

# Test types.FunctionType(..., annotations)
def test_function_type_annotations():
    # If only annotations are passed as keyword arguments, then they're
    # ignored.
    f = types.FunctionType(tf.__code

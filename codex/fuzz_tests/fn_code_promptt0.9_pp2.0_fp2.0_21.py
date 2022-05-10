fn = lambda: None
# Test fn.__code__.co_cellvars:
def fn2(b):
    z = 6
    y = lambda x: x
    y()
    a = 2 if b else 3
    y(2)
fn2.__annotations__ = {}

class TestClass: pass

# Test function to check for tuples with str in first position:
test_str_tuple_fn = lambda: None
test_str_tuple_fn.__annotations__ = {'return': (str, 'astring')}

# Test function with unknown encoding:
test_unknown_encoding_fn = lambda: None
test_unknown_encoding_fn.__annotations__ = {'return': codecs.lookup(
    'latin-1').name}

# Test function with empty __annotations__{}:
test_empty_annotations_fn = lambda: None
test_empty_annotations_fn.__annotations__ = {}

# Test filename with non--ascii chars:
def fn3(): pass
fn3.__annotations__ = {}
fn3.__annotations__

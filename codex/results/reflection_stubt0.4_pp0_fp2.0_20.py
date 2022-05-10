fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_get_code_object_from_function_with_code_attribute()
fn = lambda: None
fn.__code__ = None
fn()

# test_get_code_object_from_function_with_non_code_attribute()
fn = lambda: None
fn.__code__ = "not a code object"
fn()

# test_get_code_object_from_function_with_non_code_attribute_and_decorator()
fn = lambda: None
fn.__code__ = "not a code object"
@deco
def fn():
    pass
fn()

# test_get_code_object_from_function_with_non_code_attribute_and_decorator()
fn = lambda: None
fn.__code__ = "not a code object"
@deco
def fn():
    pass
fn()

# test_get_code_object_from_function_with_non_code_attribute_and_decorator()
fn = lambda: None
fn.__code__ = "

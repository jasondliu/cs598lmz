fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_invalid_code_object
def fn():
    pass
fn.__code__ = None
fn()

# test_invalid_code_object_2
def fn():
    pass
fn.__code__ = "not a code object"
fn()

# test_invalid_code_object_3
def fn():
    pass
fn.__code__ = []
fn()

# test_invalid_code_object_4
def fn():
    pass
fn.__code__ = 1
fn()

# test_invalid_code_object_5
def fn():
    pass
fn.__code__ = object()
fn()

# test_invalid_code_object_6
def fn():
    pass
fn.__code__ = object
fn()

# test_invalid_code_object_7
def fn():
    pass
fn.__code__ = type
fn()

# test_invalid_code_object_8
def fn():
    pass
fn.__code__ = type(

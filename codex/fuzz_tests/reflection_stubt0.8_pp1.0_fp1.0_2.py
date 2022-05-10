fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


# This raises an exception because the failure occurs when compiling the frame
# for fn.
@with_failsafe
def test_factory_unrecognized_code_object1():
    raise Exception("my exception")


# This raises an exception because the failure occurs while trying to get the
# code object.
@with_failsafe
def test_factory_unrecognized_code_object2():
    fn = lambda: None
    fn.__code__ = []
    raise Exception("my exception")


# This raises an exception because the failure occurs while trying to get the
# code object.
@with_failsafe
def test_factory_unrecognized_code_object3():
    fn = lambda: None
    fn.__code__ = 5
    raise Exception("my exception")


# This raises an exception because the failure occurs while trying to get the
# code object.
@with_failsafe
def test_factory_unrecognized_code_object4():
    fn = lambda: None
    fn.__code__ = None
    raise Exception("my

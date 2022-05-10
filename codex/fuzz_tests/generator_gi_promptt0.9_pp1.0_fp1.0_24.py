gi = (i for i in ())
# Test gi.gi_code is not None
test_continue = not_0
test_del = not_0
test_else = not_0
test_nonlocal = not_0
test_yield = not_0
# Test the default value
test_count = 0
# Test its value is not None
test_start = 0
test_step = 0
test_stop = 0
# Test its value is not None
test_type = 0


# class attrs
class TestClass(object):
    test_name = object
    test_doc = object
    test_package = object


def test_class(cls):
    for attr in dir(cls):
        if not attr.startswith('__'):
            assert hasattr(cls, attr), ("Test class %s should"
                                        " have attr %s") % (cls, attr)
            delattr(cls, attr)
    test_class.n += 1


test_class.n = 0
test_class(TestClass)

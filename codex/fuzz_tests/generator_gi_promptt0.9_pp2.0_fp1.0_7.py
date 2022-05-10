gi = (i for i in ())
# Test gi.gi_code
test_support.test_gi(gi, "gi_code", code)


class Dummy:
    pass

# Test instance method.
class SomeClass:
    def aMethod(self):
        pass

dummy = Dummy()
dummy.someInstanceMethod = SomeClass().aMethod
test_support.test_gi(dummy.someInstanceMethod, "im_self", dummy)
test_support.test_gi(dummy.someInstanceMethod, "im_class", SomeClass)
test_support.test_gi(dummy.someInstanceMethod, "im_func",
                     dummy.someInstanceMethod.__func__)
test_support.test_gi(dummy.someInstanceMethod.__func__, "__name__", "aMethod")
test_support.test_gi(dummy.someInstanceMethod, "__name__", "aMethod")

# Test builtin function.
def f():
    pass

dummy.builtin = open
test_support.test_gi(dummy.builtin.__func__, "__name__", "open

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #29095: test that the __code__ attribute of a built-in function
# is read-only.
def test_code_readonly(self):
    def check_readonly(obj, attr):
        with self.assertRaises(AttributeError):
            setattr(obj, attr, 42)
        with self.assertRaises(AttributeError):
            delattr(obj, attr)

    check_readonly(int, "__code__")
    check_readonly(int, "__qualname__")
    check_readonly(int, "__module__")
    check_readonly(int, "__annotations__")
    check_readonly(int, "__kwdefaults__")
    check_readonly(int, "__defaults__")
    check_readonly(int, "__globals__")
    check_readonly(int, "__closure__")
    check_readonly(int, "__doc__")
    check_readonly(int, "__text_signature__")


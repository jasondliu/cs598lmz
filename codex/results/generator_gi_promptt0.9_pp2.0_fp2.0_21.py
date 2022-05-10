gi = (i for i in ())
# Test gi.gi_code.co_name attribute
testEqual(gi.gi_code.co_name, '<genexpr>')
# Test gi.gi_frame.f_code.co_name attribute
testEqual(gi.gi_frame.f_code.co_name, '<module>')

# Test that generator created from a class method does not raise an
# exception when gi_code or gi_frame attributes are accessed
class FakeClass(object):
    def some_method(self, other_arg=5):
        return (i+other_arg for i in range(5))

fake_method_generator = (FakeClass().some_method(other_arg=0)).gi_frame.f_code.co_name
testEqual(fake_method_generator, 'some_method')

# Test that objects created from builtin types via the type constructor do
# not raise an exception when gi_code or gi_frame attributes are accessed
# for iteration in for loops
def builtin_iterable(lst):
    for l in lst:
        yield l



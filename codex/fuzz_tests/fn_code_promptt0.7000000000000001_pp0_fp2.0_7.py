fn = lambda: None
# Test fn.__code__.co_filename

@property
def test_1(self):
    return self.__doc__

@property
def test_2(self):
    return test_1.__doc__


test_1.__doc__ = 'foo'
test_2.__doc__ = 'bar'

print(test_1.__doc__)
print(test_2.__doc__)

test_1.__doc__ = 'foo'
test_2.__doc__ = 'bar'

print(test_1.__doc__)
print(test_2.__doc__)

test_1.__doc__ = 'foo'
test_2.__doc__ = 'bar'

print(test_1.__doc__)
print(test_2.__doc__)

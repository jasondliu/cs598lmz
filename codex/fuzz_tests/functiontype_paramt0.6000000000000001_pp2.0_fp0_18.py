from types import FunctionType
list(FunctionType(lambda x: x, globals(), "foo")(1, 2, 3))

# Test __contains__ with a string
str.__contains__("hello", "h")
str.__contains__("hello", "a")

# Test __contains__ with a list
list.__contains__([1, 2, 3], 1)
list.__contains__([1, 2, 3], 4)

# Test __contains__ with a dict
dict.__contains__({"a": 1, "b": 2}, "a")
dict.__contains__({"a": 1, "b": 2}, "c")

# Test __contains__ with an object
class F:
    def __contains__(self, item):
        return False


F.__contains__(F(), "a")

# Test __contains__ with an object
class F:
    def __contains__(self, item):
        return True


F.__contains__(F(), "a")

# Test __contains__ with an object
class F

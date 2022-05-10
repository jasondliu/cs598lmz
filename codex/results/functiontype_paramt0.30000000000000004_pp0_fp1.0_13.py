from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that __call__ is not called when calling a class
class Foo:
    def __call__(self):
        raise Exception

Foo()()

# Test that __call__ is not called when calling a class
class Foo:
    def __call__(self):
        raise Exception

Foo()()

# Test that __call__ is not called when calling a class
class Foo:
    def __call__(self):
        raise Exception

Foo()()

# Test that __call__ is not called when calling a class
class Foo:
    def __call__(self):
        raise Exception

Foo()()

# Test that __call__ is not called when calling a class
class Foo:
    def __call__(self):
        raise Exception

Foo()()

# Test that __call__ is not called when calling a class
class Foo:
    def __call__(self):
        raise Exception

Foo()()

# Test that __call__ is not called when calling a class


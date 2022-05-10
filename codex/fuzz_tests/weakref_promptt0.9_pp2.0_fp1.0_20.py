import weakref
# Test weakref.ref callbacks.


def callback(x):
    pass


def callback_exception(x):
    raise Exception("ignore me")


class Foo:
    pass


def callback_with_args(arg, x):
    arg.append(x)


def callback_with_args_kwargs(arg, x, **kwargs):
    arg.append(x)
    arg.append(kwargs.pop('key'))


def some_function():
    pass


class FooTest:

    def foo_test(self):
        """track a weakref with a callback"""
        f = Foo()
        r = weakref.ref(f, callback)
        del f
        gc.collect()
        if callback.__self__ is not None:
            raise AssertionError
        f = Foo()
        r = weakref.ref(f, callback)
        del f
        gc.collect()
        if callback.__self__() is not None:
            raise AssertionError

    def foo_test_exception(self):
        """exceptions during

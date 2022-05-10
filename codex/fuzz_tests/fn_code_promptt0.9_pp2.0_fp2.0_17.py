fn = lambda: None
# Test fn.__code__.co_freevars because we can't use fn.__closure__ on python < 3
# TODO: maybe support fn.__code__.co_freevars detections?
class _BoundIterator(_BoundArguments):
    def __init__(self, _fn, *methods, **kwargs):
        if not isinstance(_fn, types.FunctionType):
            raise TypeError('expected function, got %r' % _fn)
        super(_BoundIterator, self).__init__(_fn)

        self._closure_items = tuple(zip(self._fn.__code__.co_freevars,
                                        self._fn.__closure__))
        self._iterable = None
        self._iter = None
        self._index = 0
        self._last_value = None

        self._gathered = False
        self._full_iterations = 0

        self._expect_exhausted_at_full_iterations = kwargs.get('expect_exhausted_at_full_iterations', -1)

        self._methods = methods
        self

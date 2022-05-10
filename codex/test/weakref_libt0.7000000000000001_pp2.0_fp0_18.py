import weakref

import idaapi
import idc

from . import utils


class IDAPyLogged(object):
    """
        Decorator that allows to make a function behave like an IDAPython function.

        It will be called from IDA's context and any function called from it will be logged
        as if it was called from IDA's context.

        For example, you can use the @IDAPyLogged decorator on the following function:

        @IDAPyLogged
        def my_function(my_param):
            # ...

        And then call it from IDA's context:

        my_function(my_param)
    """
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        return self._call_with_logging(self._func, *args, **kwargs)

    def __getattr__(self, attr):
        func = getattr(self._func, attr)

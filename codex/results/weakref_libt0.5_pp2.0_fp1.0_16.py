import weakref

from . import base
from . import util
from . import const
from . import _compat


class Context(base.Object):
    """
    A context is a collection of configuration options that affect
    the behavior of the compiler.  A context is passed to the
    :meth:`Module.compile` method of a :class:`Module` to specify
    the compilation options.

    In the following example, we create a context with an empty
    configuration, and then modify it to enable the ``exceptions``
    option.

    >>> from numba import *
    >>> ctx = Context()
    >>> ctx.options
    {}
    >>> ctx.options["exceptions"] = True
    >>> ctx.options
    {'exceptions': True}

    The context can be used to compile a function:

    >>> @jit(context=ctx)
    ... def foo(x):
    ...     if x > 0:
    ...         raise ValueError
    ...     else:
    ...         return x
    ...
    >>> foo(1)
    Traceback (most recent call

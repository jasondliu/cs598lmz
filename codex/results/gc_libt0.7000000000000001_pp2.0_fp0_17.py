import gc, weakref
from collections import defaultdict

import numpy as np

def test_numba_jit_inline():
    """Test that numba_jit_inline is inline."""
    def foo(x:int)->int:
        return x*x

    assert numba_jit_inline(foo)(1) == 1
    from numba import jit
    assert foo.__module__ == '__main__'
    assert foo.__qualname__ == 'foo'
    assert foo(1) == 1
    assert foo.__dict__ == {}
    assert foo.__closure__ is None
    assert foo.__defaults__ is None
    assert foo.__annotations__ == {'x': int, 'return': int}
    assert isinstance(foo.__code__, types.CodeType)

def test_numba_jit_inline_closure():
    """Test that numba_jit_inline is inline."""
    def foo(x:int)->int:
        return x*x

    def bar(arg:int)->int:
        return foo(arg)

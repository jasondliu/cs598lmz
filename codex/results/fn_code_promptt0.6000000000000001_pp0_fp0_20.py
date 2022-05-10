fn = lambda: None
# Test fn.__code__

import sys

def f(x): return x

def test(n):
    for i in range(n):
        f.__code__

test(100000)

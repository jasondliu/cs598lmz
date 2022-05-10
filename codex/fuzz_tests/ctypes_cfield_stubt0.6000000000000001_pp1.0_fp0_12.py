import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test():
    return S.x

test.__annotations__ = {'return': ctypes.CField}

print(test())
</code>
which works fine with mypy 0.500 but fails with mypy 0.510:
<code>$ mypy 0.500.py

$ mypy 0.510.py
0.510.py:10: error: Type 'CField' is not a valid type
</code>
Is this a bug in mypy? If not, how can I annotate such a function to work with mypy 0.510?


A:

It's a bug in mypy.  Open an issue on the mypy project's github page.


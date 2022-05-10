fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


def gen():
    yield 3


fn.__code__ = gen().gi_frame.f_code

try:
    fn()
except TypeError as e:
    print(e)

try:
    f = fn.__code__.__call__
except TypeError as e:
    print(e)

# http://bugs.python.org/issue14528
import types

try:
    types.CodeType(1, 2, 3, 4, 5, 6, 7, 8, 9, 10).__call__(None, (), {})
except TypeError as e:
    print(e)

# http://bugs.python.org/issue14695
try:
    types.CodeType(1, 2, 3, 4, 5, 6, 7, 8, 9, 10).__reduce_ex__
except AttributeError as e:
    print(e)

# http://bugs.python.org/issue14695
try:
    types.CodeType(1, 2, 3, 4, 5, 6, 7, 8

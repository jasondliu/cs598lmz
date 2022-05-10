fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
"""

# test_bad_with
BAD_WITH = """\
with a:
    raise
"""

# test_bad_yield_from
BAD_YIELD_FROM = """\
def gen():
    try:
        yield
    except ZeroDivisionError:
        yield from "foo"
"""


# test_bad_yield_from_async
BAD_YIELD_FROM_ASYNC = """\
async def gen():
    try:
        await gen2()
    except ZeroDivisionError:
        yield from "foo"
async def gen2():
    return
"""


# test_bit_length_issue1669
BIT_LENGTH_ISSUE1669 = """\
class X(object):
    def __index__(self):
        return 1
x = X()
print(bin(x))
"""

# test_bool_method_descr
BOOL_METHOD_DESCR = """\
class B(object):
    def __bool__(self):
        return True
d =

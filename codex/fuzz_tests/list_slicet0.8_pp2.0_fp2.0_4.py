import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
"""
    )


def test_with_yield():
    # test recursion with generators
    run(
        """
def gen(x):
    with str(yield x) as x:
        yield x
        yield (yield x)
"""
    )


def test_loop_with_yield():
    # test recursion with generators
    run(
        """
def gen(x):
    y=x
    while y:
        with str(yield y) as y:
            yield y
            yield (yield y)
"""
    )


def test_frame_eval():
    run(
        """
def func():
    for i in range(100):
        eval('1+2')
    return eval('1+2')
"""
    )


def test_frame_exec():
    run(
        """
def func():
    for i in range(100):
        exec('pass')
    return exec('pass')
"""
    )


def test_frame_exec_assign():
    run(
        """


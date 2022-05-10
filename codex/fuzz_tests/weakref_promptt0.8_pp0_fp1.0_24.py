import weakref
# Test weakref.ref proxy objects
#
# This test module exercises weakref.ref()


class MyBase(object):
    pass


class MyKlass(MyBase):
    pass


class MyInt(int):
    pass


class MyList(list):
    pass


class MyTuple(tuple):
    pass


class MyDict(dict):
    pass


def getargs(f):
    args = getargspec(f)[0]
    argcount = len(args)
    def w(*a, **kw):
        b = a[argcount:]
        if b:
            raise TypeError('%s() takes at most %d arguments (%d given)' %
                (f.__name__, argcount, argcount + len(b)))
        return f(*a)
    return w


def check(condition, message):
    if not condition:
        raise TestFailed(message)


def check_syntax_error(testcode):
    try:
        compile(testcode, '<test string>', 'exec')
    except SyntaxError:
       

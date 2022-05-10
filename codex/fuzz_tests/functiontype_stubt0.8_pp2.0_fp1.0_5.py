from types import FunctionType
a = (x for x in [1])
b = {'a': 1}
c = FunctionType(lambda x: x, globals())


class Foo(object):
    """
    docstring
    """

    def bar(self):
        """
        docstring
        """
        print('bar')


f = Foo()

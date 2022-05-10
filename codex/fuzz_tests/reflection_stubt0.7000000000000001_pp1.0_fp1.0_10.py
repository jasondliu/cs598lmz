fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "fn"
fn.__doc__ = "fn's doc"


def f():
    """
    docstring
    """
    pass


def g():
    pass


class A:
    def __init__(self):
        pass

    def f(self):
        """
        docstring
        """
        pass

    def g(self):
        pass


class B(A):
    def __init__(self):
        pass

    def f(self):
        """
        docstring
        """
        pass

    def g(self):
        pass


class C(B):
    def __init__(self):
        pass

    def f(self):
        """
        docstring
        """
        pass

    def g(self):
        pass


class D:
    def __init__(self):
        pass

    def f(self):
        """
        docstring
        """
        pass

    def g(self):
        pass


class E(C, D):

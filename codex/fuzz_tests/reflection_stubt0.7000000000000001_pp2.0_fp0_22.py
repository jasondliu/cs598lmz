fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


class C(object):

    def __init__(self):
        self._abc_impl = abc.get_cache_token()


class A(object):

    def __init__(self):
        self._abc_impl = abc.get_cache_token()

    def __abstractmethods__(self):
        return 'f'


class B(A):
    pass


class D(object):

    def __init__(self):
        self._abc_impl = abc.get_cache_token()

    def __abstractmethods__(self):
        return 'f'


class E(D):
    pass


class F(metaclass=ABCMeta):
    pass


class G(F):
    pass


class H(metaclass=ABCMeta):
    pass


class I(metaclass=ABCMeta):
    pass


class J(H, I):

    def __init__(self):
        self._abc_impl = abc.get_cache_token()

    def __abstractmethods

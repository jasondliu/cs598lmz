gi = (i for i in ())
# Test gi.gi_code, which isn't quoted by repr().
gi.gi_code = 42
gi.gi_code = None
gi = iter(gi)


# A class for testing the ability of pickle to restore classes
# which are missing from the current environment

@attr.s
class C(object):
    foo = attr.ib()


@attr.s
class D(C):
    pass


@attr.s(init=False)
class E:
    foo = attr.ib(default=3)


def make_some_classes():
    class CA(SimpleC0):
        pass

    class CB(SimpleC0):
        pass

    class CC(SimpleC1):
        pass

    class CD(SimpleC1):
        pass

    class CE(SimpleC0):

        def __cmp__(self, other):
            return cmp(self.__dict__, other.__dict__)

    class CF(SimpleC0):

        def __cmp__(self, other):
            return cmp(self.__dict__, other.__dict__)
    return

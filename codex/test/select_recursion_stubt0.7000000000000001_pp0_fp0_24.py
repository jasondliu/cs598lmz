import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self):
            a.append('read')

    f = F()
    select.select([f], [], [])
    del f


class ABC(object):

    @abc.abstractmethod
    def foo(self, arg):
        pass

    def bar(self, arg):
        return 2 * arg


class ABCSubclass(ABC):

    def foo(self, arg):
        return 2 * self.bar(arg)


def test_abc_subclass_uninitialized():
    abc_subclass = ABCSubclass.__new__(ABCSubclass)
    assert abc_subclass.foo(2) == 4


def test_abc_subclass_initialized():
    abc_subclass = ABCSubclass()
    assert abc_subclass.foo(2) == 4


def test_abc_subclass_initialized_with_kwargs():
    abc_subclass = ABCSubclass(__abc_init=False)
    assert abc_subclass.foo(2) == 4

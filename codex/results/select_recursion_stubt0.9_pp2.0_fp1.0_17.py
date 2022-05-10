import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            if a:
                return a.pop()
            else:
                raise ValueError

    sel = select.select([F()], [], [])
    exc = raises(ValueError, sel)
    assert str(exc.value) == 'I/O operation on closed file.'

class MyFileObject:

    def __init__(self):
        self.flag = False

    def fileno(self):
        if self.flag is not True:
            self.flag = True
            return 3
        else:
            raise ValueError()


class MyOtherFileObject:

    def __init__(self):
        self.flag = False

    def fileno(self):
        if self.flag is not True:
            self.flag = True
            return 4
        else:
            raise ValueError()


def test_select_mutated2():
    sel = select.select([MyFileObject(), MyOtherFileObject()], [], [])
    assert sel[0][0].fileno() == 3
    assert sel[0][1].fileno()

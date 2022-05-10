import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0
    a.append(F())
    try:
        select.select(a,a,a)
        assert False
    except RuntimeError as e:
        assert "object mutated" in str(e)



def test_select_iter():
    class F:
        def __init__(self, l):
            self.l = l
            self.i = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.i == len(self.l):
                raise StopIteration
            self.i += 1
            return self.l[self.i - 1]
        def fileno(self):
            return self.i - 1
    a = [0]
    assert select.select(a, a, a) == (a, a, a)
    a = F([0])
    assert select.select(a, a, a) == (a, a, a)


def test_poll():
    from select import poll
    p = poll()

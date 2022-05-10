import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return self.fno
        def read(self):
            del a[-1]

    ls = []
    for i in range(select.get_max_fd() + 1):
        x = F()
        x.fno = i
        ls.append(x)
        a.append(x)

test_select_mutated()

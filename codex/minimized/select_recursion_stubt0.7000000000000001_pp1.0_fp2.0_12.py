import select
def test_select_mutated():
    a = []
    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())
    try:
        select.select(a,a,a)
    except ValueError:
        pass
if __name__ == '__main__':
    test_select_mutated()

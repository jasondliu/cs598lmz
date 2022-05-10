import select
def test_select_mutated():
    a = []
    class F:
        def fileno(self):
            test_select_mutated()
    for i in range(100):
        a.append(F())
        select.select([a[-1]], [], [], 0)
if __name__ == '__main__':
    test_select_mutated()

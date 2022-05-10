import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

        def close(self):
            a.append(1)

    select.select([F()], [], [], 0)
    for i in range(10):
        if a:
            break
        time.sleep(0.1)
    assert a == [1]

if __name__ == '__main__':
    test_select_mutated()

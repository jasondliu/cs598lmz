import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

        def __del__(self):
            a.append(4)

    for x in [7, 6, 5, 4]:
        a.append(x)
    f1 = F()
    f2 = F()
    try:
        select.select([f1, f2], [], [])
    except select.error:
        pass


if __name__ == "__main__":
    expected_error = "RuntimeError: IO operation on closed file"

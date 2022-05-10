import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())

    try:
        select.select([], [], a, 1)
    except ValueError:
        pass
    except:
        raise

def test_select_large_fd():
    # Issue #9726
    a = []
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a.append(object())
    a

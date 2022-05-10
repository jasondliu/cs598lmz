import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    f = F()
    a.append(1)
    select.select([f], [f], [f])
    a.append(2)
    select.select([f], [f], [f])
    a.append(3)
    select.select([f], [f], [f])

class F:
    def fileno(self):
        return 1

def test_select_error():
    f = F()
    del F.fileno
    try:
        select.select([f], [f], [f])
    except:
        pass

class F:
    def fileno(self):
        return -1

def test_select_bad_fd():
    f = F()
    try:
        select.select([f], [f], [f])
    except:
        pass

def test_select_closed_fd():
    f = os.open('/dev/null', os.O_RDONLY)
    os.close(f)

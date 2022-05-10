import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            if len(a) != 10:
                a.append(1)
                return F()
            else:
                return F
            raise EOFError

    select.select([F()],[],[])
    select.select([],[],[])
    select.select([],[F()],[])


def test_select_continuous_pulse():
    a = []

    class F:
        def fileno(self):
            test_select_continuous_pulse()
            if len(a) != 10:
                a.append(1)
                raise EOFError
            else:
                return F
            raise EOFError

    select.select([F()],[],[])
    select.select([],[],[])
    select.select([],[F()],[])

def test_getcwdb():
    os.getcwd()

def test_ioutil_readdir():
    import ioutils
    ioutils.ioreaddir(None)

def test_os_read():
    open('abc.123', 'w').write('ABC')
   

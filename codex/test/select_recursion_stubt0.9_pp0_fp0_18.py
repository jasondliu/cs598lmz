import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    a.append(F())
    select.select([], a, [])

def test_select_del():
    import select

    r = []
    o = range(10)
    e = []
    for i in range(4):
        r, o, e = select.select(r, o, e, 0.1)
    del r, o, e


def test_select_large_int():
    import select
    select.select([], [], [], 0x123456)
    select.select([], [], [], 0x654321)

def test_select_sec_float():
    import select

    for i in xrange(10):
        select.select([], [], [], 1.1)
        select.select([], [], [], 1.25)
        select.select([], [], [], 1.5)

def test_select_badfile():
    import select

    class BadFD(object):
        def fileno(self):
            return 'foo'
        def close(self):
            pass

   

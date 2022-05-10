import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
    try:
        select.select(a, a, a, 0)
    except:
        pass
    else:
        test_select_mutated()
    F()

def test_select():
    a = []
    for i in range(250):
        try:
            select.select(a, a, a, 0)
        except:
            pass
    if os_helper.type == os_helper.OS_TYPE_LINUX:
        import linuxaudiodev
        try:
            select.select(a, a, a, 0)
        except:
            pass

def test_bug_1043067():
    l = []
    select.select(l, l, l, 1.0)

def test_select_empty():
    # Test empty lists with and without timeout
    select.select([], [], [], None)
    select.select([], [], [], 0)

def test_select_timeout_zero():
    # Test zero length timeval objects with and without timeout
    select.select([], [

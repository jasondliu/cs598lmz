import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 2

    sel = select.select([F()], [], [])
    #print sel
    a.append(1)
    sel = select.select([], [F()], [])
    #print sel
    a.append(2)
    sel = select.select([], [], [F()])
    #print sel
    a.append(3)

    assert a == [1, 2, 3], a

def test_select_error():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 0))
    s.listen(1)
    s.close()
    try:
        select.select([s],[],[])
    except select.error:
        pass
    else:
        raise AssertionError("should raise an exception")

def test_select_timeout():
    begin = time.time()
    select.select([], [], [], 2)
    end = time.time()
    assert end-begin >= 2, "blocking

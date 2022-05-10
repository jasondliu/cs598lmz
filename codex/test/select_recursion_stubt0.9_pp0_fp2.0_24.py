import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    select.select([F()], [], [], 1)

def test_initial_call():
    select.select()

def test_return_value():
    assert select.select([], [], [], 1) == ([], [], [])

def test_return_value_event():
    assert select.select([], [], [], 1, 20) == ([], [], [])

def test_roundtrip():
    writes = os.pipe()
    readable, writable, errored = select.select([writes[0]], [writes[1]], [], 1)
    os.write(writes[1], b'\0')
    os.read(writes[0], 1)
    assert readable == []
    assert errored == []
    assert writes[0] in writable

def test_timeout():
    start = time.time()
    select.select([], [], [], 1)
    assert abs(time.time() - start - 1) <= 0.05


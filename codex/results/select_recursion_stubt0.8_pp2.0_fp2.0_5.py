import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    select.select([], [], [F()], 1)

def test_select_addwait_mutated():
    class F:
        def fileno(self):
            test_select_addwait_mutated()

    r, w = os.pipe()
    try:
        asyncio.get_event_loop().add_writer(w, test_select_addwait_mutated)
        os.write(w, b"x")
    finally:
        os.close(w)
        os.close(r)
    asyncio.wait([asyncio.Future()])

def test_wait_mutated():
    class F:
        def add_done_callback(self, cb):
            loop = asyncio.get_event_loop()
            loop.call_soon(test_wait_mutated, loop)

    asyncio.wait([F()])

def test_wait_cancel_mutated():
    class F:
        def cancel(self):
            loop = asyncio.get_event_loop()
            loop.call_soon(

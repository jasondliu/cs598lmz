import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [])

def test_select_interrupted():
    class F:
        def fileno(self):
            return 42

    select.select([F()], [], [])

def test_select_interrupted_2():
    class F:
        def fileno(self):
            return 42

    def f():
        select.select([F()], [], [])

    t = threading.Thread(target=f)
    t.start()
    time.sleep(0.1)
    t.join()

def test_select_interrupted_3():
    class F:
        def fileno(self):
            time.sleep(0.1)
            return 42

    t = threading.Thread(target=test_select_interrupted_2)
    t.start()
    time.sleep(0.1)
    t.join()

def test_select_interrupted_4():
    class F:
        def fileno(self):
            time.sleep(0.1)
           

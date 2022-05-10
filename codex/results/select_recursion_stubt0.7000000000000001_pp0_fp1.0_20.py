import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def close(self):
            test_select_mutated()

    f = F()
    select.select([f], [], [])

try:
    select.devpoll
except AttributeError:
    pass
else:
    def test_devpoll_mutated():
        from select import devpoll
        a = []
        class F:
            def fileno(self):
                test_devpoll_mutated()
                return len(a)
        f = F()
        dp = devpoll.fromfd(f)
        dp.close()
        # mutate objects during close()
        test_devpoll_mutated()

def test_main():
    test_select_mutated()
    try:
        test_devpoll_mutated()
    except NameError:
        pass

if __name__ == "__main__":
    test_main()

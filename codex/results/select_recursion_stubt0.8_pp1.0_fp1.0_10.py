import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            del a[:]
            return 3
        def close(self):
            raise Exception

    select.select([F()], [F()], [F()])

if 0 and hasattr(select, "poll"):
    def test_poll_mutated():
        a = []

        class F:
            def fileno(self):
                test_poll_mutated()
                del a[:]
                return 3
            def close(self):
                raise Exception

        select.poll().poll([F()])

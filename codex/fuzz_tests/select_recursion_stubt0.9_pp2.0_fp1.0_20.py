import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return None
        def close(self):
            pass
    a.append(f=F())
    select.select([],[a],[])

try:
    select.poll()
except:
    pass
else:
    def test_poll_mutated():
        a = []

        class F:
            def fileno(self):
                test_poll_mutated()
                return None
            def close(self):
                pass
        a.append(f=F())
      

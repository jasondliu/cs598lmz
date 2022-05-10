import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            return 0

    F()  # creates a new cycle
    def gc_collect():
        for i in range(10):
            # The following line may cause a segfault if
            # select_mutated() is not called.
            select.select([], [], [], 0.1)
            if not hasattr(F, '__del__'):
                # The cycle has been broken
                return
            gc.collect()
    gc_collect()

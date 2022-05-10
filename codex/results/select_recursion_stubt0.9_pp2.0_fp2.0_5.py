import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # This will mutate the list!
            return 0
    a.append(F())

    try:
        select.select([], [], a)
    except:
        pass


if __name__=='__main__':
    test_select_mutated()
    test_select_mutated()
</code>


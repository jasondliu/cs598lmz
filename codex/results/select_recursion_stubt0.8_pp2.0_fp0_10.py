import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # this sub call mutates the list 'a'
            return 5

    select.select([F()], [], [])
    #assert_raises(select.error, select.select, a, a, a, 0)
    #assert_raises(select.error, select.select, a, a, a, 1.2)

import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    f = F()
    l = [f]
    select.select(l, l, l)
    a.append(l)

    # make sure we didn't mutate the list object
    assert l is not a[0]
    # make sure we didn't mutate the file object
    assert l[0] is f

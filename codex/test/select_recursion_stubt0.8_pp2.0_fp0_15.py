import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    # Issue #10103
    #
    # Ensure that select does not mutate the list passed in
    #
    # It used to consume a generator passed to it.
    fd = F()
    select.select([fd], [], [], 0)
    assert a == [1]
    select.select([fd], a, [], 0)
    assert a == [1]
    select.select([fd], a, a, 0)
    assert a == [1, 1]

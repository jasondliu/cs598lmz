import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

    f = F()

    select.select([f], [], [])

def test_select_list_mutated_in_callback():
    class F:
        def fileno(self):
            # mutate a list that was passed to select
            del a[:]
            return 1

    f = F()

    a = [f]
    select.select(a, a, a)

def test_select_list_item_mutated_in_callback():
    class F:
        def fileno(self):
            # mutate an item from a list that was passed to select
            del a[0]
            return 1

    f = F()

    a = [f, f]
    select.select(a, a, a)

def test_select_list_item_mutated_in_callback_2():
    class F:
        def fileno(self):
            # mutate an item from a list that was passed to select
            a[0] = None
            return 1

    f = F()


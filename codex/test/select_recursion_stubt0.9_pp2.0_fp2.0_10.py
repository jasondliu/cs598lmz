import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    f = F()
    try_array_to_string([select.select([f], a, a, 1)], 'select')
    test_select_mutated()

    # Repeated calls to select mutate the argument lists.
    try_array_to_string([select.select([], a, a, 0.0)], 'select')
    test_select_mutated()
    try_array_to_string([select.select([f], a, a, 0.0)], 'select')
    test_select_mutated()
    try_array_to_string([select.select([], a, a, 0.0)], 'select')
    test_select_mutated()
    try_array_to_string([select.select([f], a, a, 0.0)], 'select')
    test_select_mutated()

def test_epoll():
    e = select.epoll()
    e.poll(-1)
    e.fileno()

    p = select.poll()
    p.poll(-1)
   

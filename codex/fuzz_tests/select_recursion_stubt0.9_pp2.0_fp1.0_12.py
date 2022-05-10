import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()  # recursion
            return 3

    try:
        select.select([], [], [F()], 1)
    except RecursionError:
        pass
    else:
        a.append(1)
    try:
        select.select([], [], [F()], 1)
    except RecursionError:
        pass
    else:
        a.append(2)

    if not a:
        raise ValueError("never called recursively")

# ----------------------------------------------------
# Tuple errors when calling select (pos and neg numbers)
# ----------------------------------------------------

import select

def test_select_tuple():
    a = select.select((1, 0), (1, -1, -3, -3), (), 1)
    if a != ([1], [1], []):
        raise ValueError(a)
# -----
# Poll object
# -----

import select

def test_poll():
    p = select.poll()
    p.poll()
    a = p.poll(1)
    if a:
        raise ValueError(a)

# ----------------

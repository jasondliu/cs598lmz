import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([1, 2], [], [], 0)
    select.select([1, 2], [], [], 0)
    select.select([1, 2], [], [], 0)
    select.select([1, 2], [], [], 0)
    select.select([1, 2], [], [], 0)
    select.select([1, 2], [], [], 0)
    select.select([1, 2], [], [], 0)
    select.select([1, 2], [], [], 0)
    select.select([1, 2], [], [], 0)
    try:
        select.select([1, 2], [], [], 0)
    except select.error:
        print('select.error')
    try:
        select.select([1, 2], [], [], 0)
    except select.error:
        print('select.error')
    try:
        select.select([1, 2], [], [], 0)
    except select.error:
        print('select.error')
   

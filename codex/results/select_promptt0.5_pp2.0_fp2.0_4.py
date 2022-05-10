import select
# Test select.select()

def test_select():
    import time
    import select

    # Test a simple read
    r, w, x = select.select([sys.stdin], [], [], 0.1)
    if sys.stdin in r:
        s = sys.stdin.readline()
        print 'You entered', s

    # Test a simple write
    r, w, x = select.select([], [sys.stdout], [], 0.1)
    if sys.stdout in w:
        sys.stdout.write('this writes to stdout\n')

    # Test an exceptional condition
    r, w, x = select.select([sys.stdin], [], [sys.stdin], 0.1)
    if sys.stdin in x:
        print 'exceptional'

    # Test a timeout
    r, w, x = select.select([sys.stdin], [], [], 2.0)
    if not r and not w and not x:
        print 'timeout'

    # Test a read that is interrupted by a signal
    try:

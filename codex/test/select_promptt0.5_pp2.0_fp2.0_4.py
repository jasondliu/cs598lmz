import select
# Test select.select()

def test_select():
    import time
    import select

    # Test a simple read
    r, w, x = select.select([sys.stdin], [], [], 0.1)
    if sys.stdin in r:
        s = sys.stdin.readline()

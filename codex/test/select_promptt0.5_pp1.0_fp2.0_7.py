import select
# Test select.select

def test_select():
    read, write, err = select.select([sys.stdin], [], [], 10)

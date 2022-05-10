import select
# Test select.select

def test_select():
    print("Testing select.select()...")
    read_list = []
    write_list = []
    error_list = []
    timeout = 1
    print("Calling select.select() with timeout = 1...")
    readable, writable, errored = select.select(read_list, write_list, error_list, timeout)
    print("select.select() returned")
    print("  readable: %s" % readable)
    print("  writable: %s" % writable)
    print("  errored: %s" % errored)
    print("Calling select.select() with timeout = 0...")
    readable, writable, errored = select.select(read_list, write_list, error_list, 0)
    print("select.select() returned")
    print("  readable: %s" % readable)
    print("  writable: %s" % writable)
    print("  errored: %s" % errored)
    print("Calling select.select() with timeout = None...")
    readable,

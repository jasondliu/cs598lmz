import select
# Test select.select()
def test_select():
    import time
    import select

    read_list = []
    write_list = []
    error_list = []
    timeout = 1

    while True:
        # select.select(rlist, wlist, xlist[, timeout])
        read_ready, write_ready, error_ready = select.select(read_list, write_list, error_list, timeout)

        if read_ready:
            print("There is something to read")
        if write_ready:
            print("There is something to write")
        if error_ready:
            print("There is an error")

        time.sleep(timeout)

test_select()

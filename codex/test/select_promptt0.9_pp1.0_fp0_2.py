import select
# Test select.select and poll.poll()

if 1:  # test select.select()
    def sel():
        readers, writers, errr = select.select([], [], [], 0)
        if errr:
            raise Exception("ERROR")

    def sel_wait(rlist, wlist, xlist, timeout=None):
        readers, writers, errr = select.select(rlist, wlist, xlist, timeout)
        if errr:
            raise Exception("ERROR")
        return readers, writers

    select_wait = sel_wait
else:  # test select.poll()
    from select import poll, POLLERR, POLLHUP
    p = poll()

    def sel():
        for fd, event in p.poll(0):
            if event & POLLERR:
                raise Exception("ERROR")

    def sel_wait(rlist, wlist, xlist, timeout=None):
        readers = set(rlist)
        writers = set(wlist)

import select
# Test select.select function
def select_test():
    epoll = select.epoll()
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    while True:
        epoll_list = epoll.poll()
        for fd, events in epoll_list:
            if fd == sys.stdin.fileno():
                msg = sys.stdin.readline()
                print(msg)


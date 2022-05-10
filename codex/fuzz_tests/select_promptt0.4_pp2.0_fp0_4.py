import select
# Test select.select()

def select_test():
    print("select_test")
    start_time = time.time()
    while True:
        print("select...")
        rlist, wlist, xlist = select.select([], [], [], 5)
        if time.time() - start_time > 10:
            print("done")
            break

select_test()

# Test select.poll()

def poll_test():
    print("poll_test")
    start_time = time.time()
    p = select.poll()
    while True:
        print("poll...")
        p.poll(1000)
        if time.time() - start_time > 10:
            print("done")
            break

poll_test()

# Test select.epoll()

def epoll_test():
    print("epoll_test")
    start_time = time.time()
    e = select.epoll()
    while True:
        print("epoll...")
        e.poll(1000)
        if time.time() - start_

import threading
# Test threading daemon.


def f(a):
    time.sleep(a)
    print("%s:%s" % ("thread", a))
    time.sleep(a)


if __name__ == '__main__':
    print("aaaa")
    for i in range(4):
        p = threading.Thread(target=f, args=(i,))
        # p.setDaemon(True)
        p.start()
    print("bbbb")
    time.sleep(2)
    print("cccc")
# Test threading with decorator.


def test_threading_with_func_decorator(sleeping_time):
    def test_threading_decorator(f):
        def wrapper():
            import threading
            t = threading.Thread(target=f)
            t.start()
            time.sleep(sleeping_time)
        return wrapper
    return test_threading_decorator


@test_threading_with_func_decorator(2)
def test_threading_with_func_decorator_

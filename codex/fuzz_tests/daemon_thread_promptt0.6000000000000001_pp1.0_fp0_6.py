import threading
# Test threading daemon
#
if __name__ == '__main__':
    import time
    import threading

    def worker():
        print("{} start".format(threading.current_thread().getName()))
        time.sleep(5)
        print("{} stop".format(threading.current_thread().getName()))

    def worker2():
        print("{} start".format(threading.current_thread().getName()))
        time.sleep(100)
        print("{} stop".format(threading.current_thread().getName()))

    t = threading.Thread(name="worker", target=worker)
    t2 = threading.Thread(name="worker2", target=worker2)

    t.daemon = True
    t2.daemon = True

    t.start()
    t2.start()

    t.join()
    t2.join()

    print("{} end".format(threading.current_thread().getName()))


# if __name__ == '__main__':
#     import time
#     import

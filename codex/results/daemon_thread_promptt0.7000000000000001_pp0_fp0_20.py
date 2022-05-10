import threading
# Test threading daemon
# from threading import Thread
def daemon_thread(i):
    threading.current_thread().name = "DAEMON-"+str(i)
    time.sleep(1)
    print("Thread: {}, Time: {}".format(threading.current_thread().name, time.ctime()))

# if __name__ == "__main__":
#     for i in range(10):
#         t = Thread(target=daemon_thread, args=[i])
#         t.setDaemon(True)
#         t.start()
#         t.join()
#     print("Done!")


## 11.3.3 引入生成器 ##
# yield 与 yield from
def gen_func():
    yield 1
    yield 2
    yield 3

def gen_func2():
    value = yield 1
    print("Value: ", value)
    value = yield 2
    print("Value: ", value)
    yield 3

# if __name__ == "__main__":
#     gen = gen_func

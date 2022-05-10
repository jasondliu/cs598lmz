import threading
# Test threading daemon
def f1(text):
    print("f1 started")
    for i in range(5):
        print("f1:", text, i)
        print("f1 alive:", threading.main_thread().is_alive())
        time.sleep(1)
    print("f1 finished")


def f2(text):
    print("f2 started")
    for i in range(5):
        print("f2:", text, i)
        print("f2 alive:", threading.main_thread().is_alive())
        time.sleep(1)
    print("f2 finished")


def f3(text):
    print("f3 started")
    for i in range(5):
        print("f3:", text, i)
        print("f3 alive:", threading.main_thread().is_alive())
        time.sleep(1)
    print("f3 finished")


t1 = threading.Thread(target=f1, args=("t1",))
t2 = threading.Thread(target=f2

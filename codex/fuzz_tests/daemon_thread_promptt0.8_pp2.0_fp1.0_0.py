import threading
# Test threading daemon
print("Stat main thread: ", threading.current_thread())

def test1():
    print("Stat test1 thread: ", threading.current_thread())
    print("test1: sleep")
    time.sleep(3)
    print("test1: wakeup")
    print("test1: end")

def test2():
    print("Stat test2 thread: ", threading.current_thread())
    print("test2: sleep")
    time.sleep(10)
    print("test2: wakeup")
    print("test2: end")

print("Start test1 thread")
t1 = threading.Thread(target=test1, name="T1", daemon=True)
t1.start()
print("Start test2 thread")
t2 = threading.Thread(target=test2, name="T2")
t2.start()
print("All thread start")
while True:
    time.sleep(0.5)
    print("Main: sleep 0.5s")
    if t1.is_alive():
        print("T1 is alive

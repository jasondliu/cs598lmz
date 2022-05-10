import threading
# Test threading daemon
def run_thread(name):
    print("Thread %s is running" % name)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=run_thread, args=("t1",))
    t2 = threading.Thread(target=run_thread, args=("t2",))
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Main thread ends")

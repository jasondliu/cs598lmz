import threading
# Test threading daemon
def run():
    print("thread is running")
    print("thread id:",threading.current_thread().name)
    time.sleep(2)
    print("thread is over")

if __name__ == '__main__':
    print("main thread is running")
    print("main thread id:", threading.current_thread().name)
    t = threading.Thread(target=run,name="my_thread")
    t.setDaemon(True)
    t.start()
    t.join()
    print("main thread is over")

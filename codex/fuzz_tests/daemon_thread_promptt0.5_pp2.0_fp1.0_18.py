import threading
# Test threading daemon

def run_thread(thread_name):
    print(thread_name)
    for i in range(10):
        time.sleep(0.5)
        print(thread_name, i)

thread1 = threading.Thread(target=run_thread, args=("Thread1",))
thread1.setDaemon(True)
thread2 = threading.Thread(target=run_thread, args=("Thread2",))
thread2.setDaemon(True)
thread1.start()
thread2.start()

# thread1.join()
# thread2.join()

print("Done")

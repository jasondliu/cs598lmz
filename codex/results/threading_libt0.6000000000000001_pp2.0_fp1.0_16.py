import threading
threading.Thread(target=run_thread, args=("Thread-3", 4)).start()

for i in range(5):
    print("MainThread:", i)
    time.sleep(1)

print("Done")

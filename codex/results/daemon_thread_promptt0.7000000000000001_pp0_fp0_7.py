import threading
# Test threading daemon
def thread_function():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')

# Create a thread
x = threading.Thread(target=thread_function, daemon=True)
# Start the thread
x.start()

# Join the thread
x.join()
print("Done!")

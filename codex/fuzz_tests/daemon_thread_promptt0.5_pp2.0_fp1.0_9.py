import threading
# Test threading daemon

def my_func():
    print("Started")
    time.sleep(5)
    print("Finished")

thread = threading.Thread(target=my_func)
thread.daemon = True
thread.start()

print("Main thread")

time.sleep(1)

if thread.is_alive():
    print("Thread is alive")
else:
    print("Thread is dead")

print("End of main thread")

# Test threading daemon

import threading

def my_func():
    print("Started")
    time.sleep(5)
    print("Finished")

thread = threading.Thread(target=my_func)
thread.start()

print("Main thread")

time.sleep(1)

if thread.is_alive():
    print("Thread is alive")
else:
    print("Thread is dead")

print("End of main thread")

# Test threading daemon

import threading

def my_func():
    print("Started")
    time.sleep(5

import threading
# Test threading daemon
# This is just a test because it doesn't stop
# def threading_function(name):
#     while True:
#         print(name)
#         time.sleep(1)
#
# thread1 = threading.Thread(target=threading_function,args=("Thread 1",))
# thread1.setDaemon(True) #Making it a dameon thread
# thread1.start()
#
# # This will not run because the main thread quits
# # It knows there are no non daemon threads left
# thread1.join()

# It's also possible to stop threads - Threads can't be stopped
def threading_function(name):
    print(name)
    time.sleep(1)
    raise SystemExit

# If there are no non daemons running the main thread will quit
# If there are non daemons running it will not quit
thread1 = threading.Thread(target=threading_function,args=("Thread 1",))
thread1.start()
thread1.join()


# File access - Nice and simple
# Open a file,

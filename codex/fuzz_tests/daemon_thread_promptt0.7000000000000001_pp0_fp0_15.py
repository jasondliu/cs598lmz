import threading
# Test threading daemon 
# To stop the code run, set daemon to True
def worker():
    for i in range(5):
        print(threading.current_thread().name,i)
        time.sleep(1)

t1=threading.Thread(target=worker)
t1.setDaemon(True)
t1.start()
print(threading.current_thread().name)
print(threading.active_count())

for i in range(3):
    print(threading.current_thread().name,i)

# This code will only run the child process and not the parent process.
# This is because the daemon is set to True.

# output
# MainThread
# 2
# MainThread 0
# MainThread 1
# MainThread 2
# Thread-1 0
# Thread-1 1
# Thread-1 2
# Thread-1 3
# Thread-1 4

# All the lines in the output are not in the same order if we run the code multiple times
# If we set daemon = False, the output will be:
# MainThread
# 2
# Main

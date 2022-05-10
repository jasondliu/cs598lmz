import sys, threading

def run():
    print("Thread: {}".format(threading.current_thread().name))
    sys.exit()

thread = threading.Thread(target=run)
thread.start()

print("Main: {}".format(threading.current_thread().name))

# Thread: Thread-1
# Main: MainThread

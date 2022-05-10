import sys, threading
threading.Thread(target=lambda: sys.stdout.write("[$] Thread 1 started\n")).start()
threading.Thread(target=lambda: sys.stdout.write("[$] Thread 2 started\n")).start()

# Non-blocking; use threads
import sys, threading
threading.Thread(target=lambda: sys.stdout.write("[$] Thread 1 started\n")).start()
threading.Thread(target=lambda: sys.stdout.write("[$] Thread 2 started\n")).start()
sys.stdout.write("[>] I'm not blocked\n")

# Thread execution
import sys, threading
def thread_func(v):
    sys.stdout.write("[*] Thread %s started\n" % v)
    for i in range(4):
        sys.stdout.write("[*] Thread %s executing...\n" % v)
threading.Thread(target=thread_func, args=(1,)).start()
threading.Thread(target=thread_func, args=(2,)).start()

# Thread variables


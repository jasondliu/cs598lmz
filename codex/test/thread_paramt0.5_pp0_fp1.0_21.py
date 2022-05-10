import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from the other thread\n")).start()

# The above is equivalent to:
def hello_from_other_thread():
    sys.stdout.write("Hello from the other thread\n")
threading.Thread(target=hello_from_other_thread).start()

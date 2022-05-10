import sys, threading
threading.Thread(target=lambda: sys.stderr.write("My first thread!\n")).start()

def thread_function(name):
    print("Thread %s: starting" % name)
    time.sleep(2)
    print("Thread %s: finishing" % name)

if __name__ == "__main__":
    # Start threads
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()

    # Wait for threads to finish
    x.join()

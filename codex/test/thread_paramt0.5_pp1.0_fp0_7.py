import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# Example of multithreading with a function
def thread_function(name):
    print("Thread %s: starting" % name)
    time.sleep(2)
    print("Thread %s: finishing" % name)

if __name__ == "__main__":
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()
    y = threading.Thread(target=thread_function, args=(2,))
    y.start()
    x.join()
    y.join()

# Example of multithreading with a class
class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """


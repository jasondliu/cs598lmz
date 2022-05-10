import threading
# Test threading daemon process
import time

def thread_function(name):
    print("Thread {}: starting".format(name))
    time.sleep(2)
    print("Thread {}: finishing".format(name))

if __name__ == "__main__":
    x = threading.Thread(target=thread_function, args=(1,))
    y = threading.Thread(target=thread_function, args=(2,))
    x.start()
    y.start()
    x.join()
    y.join()

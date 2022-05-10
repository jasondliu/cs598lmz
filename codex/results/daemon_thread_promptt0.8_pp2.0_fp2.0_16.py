import threading
# Test threading daemon
from time import sleep
import os


def thread_function(name):
    while True:
        print("Thread {}: starting".format(name))
        sleep(5)
        print("Thread {}: finishing".format(name))


if __name__ == "__main__":
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    y = threading.Thread(target=thread_function, args=(2,), daemon=True)
    z = threading.Thread(target=thread_function, args=(3,))
    x.start()
    y.start()
    z.start()
    print("main thread")
    z.join()
    print("main thread: ending")

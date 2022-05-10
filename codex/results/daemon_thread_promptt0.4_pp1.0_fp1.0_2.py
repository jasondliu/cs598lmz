import threading
# Test threading daemon
# https://stackoverflow.com/questions/20339256/threading-in-python-3-2

def my_func(name):
    print("Thread %s: starting" % name)
    time.sleep(2)
    print("Thread %s: finishing" % name)

if __name__ == "__main__":

    print("Main    : before creating thread")
    x = threading.Thread(target=my_func, args=("A",))
    print("Main    : before running thread")
    x.start()
    print("Main    : wait for the thread to finish")
    # x.join()
    print("Main    : all done")

# Main    : before creating thread
# Main    : before running thread
# Main    : wait for the thread to finish
# Thread A: starting
# Thread A: finishing
# Main    : all done

# Main    : before creating thread
# Main    : before running thread
# Main    : wait for the thread to finish
# Main    : all done
# Thread A: starting
# Thread A: finishing

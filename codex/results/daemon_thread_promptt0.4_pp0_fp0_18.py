import threading
# Test threading daemon

def thread_function():
    print("Thread {} started".format(threading.get_ident()))
    time.sleep(2)
    print("Thread {} ended".format(threading.get_ident()))

if __name__ == '__main__':
    threads = list()
    for index in range(3):
        print("Main    : create and start thread {}".format(index))
        x = threading.Thread(target=thread_function)
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        print("Main    : before joining thread {}".format(index))
        thread.join()
        print("Main    : thread {} done".format(index))

# Main    : create and start thread 0
# Main    : create and start thread 1
# Main    : create and start thread 2
# Thread 139831009554944 started
# Thread 139831009554944 ended
# Main    : before joining thread 0
# Thread 139831009554944 started
# Thread 13983

import threading
# Test threading daemon
def thread_function(name):
    # print(threading.main_thread())
    print("Thread %s: starting", name)
    time.sleep(2)
    # print(threading.main_thread())
    print("Thread %s: finshed", name)


if __name__ == "__main__":

    # for i in range(3):
    #     x = threading.Thread(target=thread_function, args=(i,))
    #     x.start()

    # without daemon
    # threads = list()
    # for index in range(3):
    #     print("Main    : create and start thread %d." % index)
    #     x = threading.Thread(target=thread_function, args=(index,))
    #     threads.append(x)
    #     x.start()

    # with daemon
    threads = list()
    for index in range(3):
        print("Main    : create and start thread %d." % index)
        x = threading.Thread(target=thread_function, args=(index,))


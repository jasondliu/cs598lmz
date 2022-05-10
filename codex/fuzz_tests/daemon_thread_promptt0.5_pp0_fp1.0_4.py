import threading
# Test threading daemon

def thread_function(name):
    print("Thread {} started".format(name))
    x = 0
    while True:
        time.sleep(1)
        print("{}: {}".format(name, x))
        x += 1

if __name__ == "__main__":
    threads = list()
    for index in range(3):
        print("Main    : create and start thread {}".format(index))
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        print("Main    : before joining thread {}".format(index))
        thread.join()
        print("Main    : thread {} done".format(index))

import threading
threading.stack_size(67108864)

def function(x):
    return x * x

def thread_function(name):
    print("Thread %s: starting" % name)
    time.sleep(2)
    print("Thread %s: finishing" % name)

if __name__ == "__main__":
    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #     executor.map(function, range(10))
    #     executor.submit(function,5)
    #     executor.submit(function,6)
    #     executor.submit(function,7)

    x = threading.Thread(target=thread_function, args=(1,))
    y = threading.Thread(target=thread_function, args=(2,))
    x.start()
    y.start()
    x.join()
    y.join()

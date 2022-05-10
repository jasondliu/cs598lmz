import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def context_switching_speed():
    '''
    This functions tests the time it takes for the Python interpreter to switch
    between different execution contexts. This is achieved by creating a number
    of threads and starting them. Python switches to the other thread, waits for
    it to finish and then switches back.
    '''
    threads = []
    for i in range(5):
        func = FUNTYPE(lambda:None)
        thread = threading.Thread(target=func)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

def run_tests():
    threading_speed()
    context_switching_speed()
    print("Tests finished")

if __name__ == '__main__':
    run_tests()

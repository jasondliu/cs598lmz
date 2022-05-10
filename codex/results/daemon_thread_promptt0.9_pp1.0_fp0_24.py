import threading
# Test threading daemon function
def work():
    print('working')
    time.sleep(2)


def test():
    n = 100
    for i in range(n):
        t = threading.Thread(target=work)
        t.setDaemon(True)
        t.start()
        #t.join()
    time.sleep(10)


if __name__ == '__main__':
    test()
    #test_queue_open()
    #test_queue()
    #test_dirs()
    #test_threads()
    #test_download()

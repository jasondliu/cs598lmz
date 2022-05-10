import threading
# Test threading daemon

#
# def myThread(i):
#     print('Thread {} started'.format(i))
#     time.sleep(2)
#     print('Thread {} finished'.format(i))
#
# for i in range(10):
#     t = threading.Thread(target=myThread, args=(i,))
#     t.setName('Thread #{}'.format(i))
#     t.setDaemon(True)
#     t.start()
#     # t.join()
#
# print('Main thread finished')

# Test multiprocessing daemon
def myThread(i):
    print('Thread {} started'.format(i))
    time.sleep(2)
    print('Thread {} finished'.format(i))

if __name__ == '__main__':
    for i in range(10):
        p = mp.Process(target=myThread, args=(i,))
        p.setName('Thread #{}'.format(i))
        p.daemon = True
        p.start()
        p.join()
    print

import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('exit')

if __name__ == '__main__':
    t = threading.Thread(target=test_daemon)
    t.setDaemon(True)
    t.start()
    print('main thread')
    time.sleep(1)
    print('main thread')

# Test threading lock
# lock = threading.Lock()
# def run_thread(n):
#     lock.acquire()
#     print('thread', n)
#     lock.release()
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=run_thread, args=(1,))
#     t2 = threading.Thread(target=run_thread, args=(2,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print('main thread')

# Test threading local
# local_school = threading.

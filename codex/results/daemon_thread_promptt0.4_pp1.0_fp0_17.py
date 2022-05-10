import threading
# Test threading daemon
def test_thread_daemon():
    # 创建一个线程实例
    t = threading.Thread(target=thread_job, name='T1')
    # 守护线程
    t.setDaemon(True)
    t.start()
    print('all done')

# Test threading join
def test_thread_join():
    # 创建一个线程实例
    t = threading.Thread(target=thread_job, name='T1')
    t.start()
    t.join()
    print('all done')

# Test threading lock
def test_thread_lock():
    # 创建一个线程实例
    t = threading.Thread(target=thread_job, name='T1')
    t.start()
    print('all done')

# Test threading lock
def test_thread_lock():
    #

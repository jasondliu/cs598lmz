import threading
# Test threading daemon
# thread is terminated by python interpreter exit
def func(a):
    print('Thread is executed, parameters:'+a)

if __name__ == '__main__':
    t = threading.Thread(name='test_thread',target=func,args=('123',))
    t.setDaemon(True) # daemon thread
    t.start()
    print('Started thread')

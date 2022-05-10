import threading
threading.stack_size(67108864) # 64MB stack
print 'START'
def print_time(threadName):
    print '${}'.format(threadName)
    print 'GTK_MAIN_QUIT'
thread = threading.Thread(target=print_time, args=("Thread-1",))
#thread = threading.Thread(group=None, target=print_time, name='Thread-1', args=("Thread-1",))
thread.start()
thread.join()

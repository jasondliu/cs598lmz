import threading
# Test threading daemon
def my_thread(name):
    print('Start ' + name)
    time.sleep(1)
    print('End ' + name)

my_thread('test')

t1 = threading.Thread(target=my_thread, name='test1', args=('test1',))
t1.daemon = True
t1.start()
t1.join()
print('End of main thread')

print('-'*20)

# Test threading no daemon
def my_thread(name):
    print('Start ' + name)
    time.sleep(1)
    print('End ' + name)

my_thread('test')

t1 = threading.Thread(target=my_thread, name='test1', args=('test1',))
t1.daemon = False
t1.start()
t1.join()
print('End of main thread')

print('-'*20)

# Test threading no daemon
def my_thread(name):
    print('Start ' + name)
    time.sleep(1)
    print

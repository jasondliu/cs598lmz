import threading
# Test threading daemon mode
def worker():
    t_name = threading.currentThread().getName()
    p = multiprocessing.current_process().name
    print(f'child thread:{t_name} of process:{p}')
    print(f'child is alive:{threading.currentThread().is_alive()}')
    time.sleep(2)

def do():
    t_name = threading.currentThread().getName()
    p = multiprocessing.current_process().name
    print(f'Main thread:{t_name} from process:{p}')
    print(f'Main is alive:{threading.currentThread().is_alive()}')

def test_daemon():
    t = threading.Thread(target=worker, name = 'mythread')
    t.setDaemon(True)
    t.start()
    time.sleep(1)
    do()

# Test Enumerate
def foo():
    print(f'foo of {threading.currentThread().name} is running')
    time.sleep(2)
   

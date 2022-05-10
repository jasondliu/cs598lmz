import sys, threading

def run():
    while True:
        sys.stdout.write('%s\n' % threading.current_thread().name)
        sys.stdout.flush()


t1 = threading.Thread(target=run, name='Thread1')
t2 = threading.Thread(target=run, name='Thread2')
t3 = threading.Thread(target=run, name='Thread3')
print(threading.current_thread())
print(t1.is_alive())
t1.start()
t2.start()
t3.start()
print(t1.is_alive())
print(t1.name)
print(t2.name)
print(threading.enumerate())
print(threading.active_count())

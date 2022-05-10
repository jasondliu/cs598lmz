import threading
# Test threading daemon.
# run
def action(max):
    for i in range(max):
        sleep(1)
        print(threading.current_thread().getName() + '-' + str(i))

#Main threading
t1 = threading.Thread(target=action, args=(100,))
t1.start()
t1.join(timeout=20)
print(t1.getName(), '\t', t1.is_alive())
t2 = threading.Thread(target=action, args=(100,))
t2.setDaemon(True)
t2.start()
t2.join(timeout=20)
print(t2.getName(), '\t', t2.is_alive())

import threading
# Test threading daemon
def daemon():
    print('starting daemon')
    time.sleep(2)

t = threading.Thread(target=daemon)
t.setDaemon(True) # daemon need to be set before it is started
t.start()

print('Checking thread is alive', t.is_alive())
print('Checking daemon is alive', t.is_alive())

t.join() # wait for the thread to end
print('Checking thread is alive', t.is_alive())
print('Checking daemon is alive', t.is_alive())

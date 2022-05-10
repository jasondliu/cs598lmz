import threading
# Test threading daemon mode

def fun():
    print ('start fun')
    time.sleep(2)
    print ('end fun')

print ('start')

thread = threading.Thread(target=fun)
thread.setDaemon(True)
thread.start()

print ('end')

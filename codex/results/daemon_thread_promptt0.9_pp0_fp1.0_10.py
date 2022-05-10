import threading
# Test threading daemonica
def job():
    print("This is job!")
    print("Current: "+threading.current_thread().getName())
a =threading.Thread(target=job,name='Daemon Thread')
a.setDaemon(True)
b =threading.Thread(target=job,name=' Non-Daemon Thread')
b.setDaemon(False)
a.start()
b.start()

b.join()
print("This is end!")

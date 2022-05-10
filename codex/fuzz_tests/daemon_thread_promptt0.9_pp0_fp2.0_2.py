import threading
# Test threading daemon/non daemon thread
class myThread(threading.Thread):
    def run(self):
        for i in range(3):
            print(i)
            sleep(1)
# Non daemon Thread
t = myThread(name = 'non-daemon')
t.setDaemon(False)
t.start()
t.join()
print('\n')

# daemon thread
dt = myThread(name = 'daemon')
dt.setDaemon(True)
dt.start()
dt.join()

print('end of main thread')

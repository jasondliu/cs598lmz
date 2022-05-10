import threading
# Test threading daemon mode
def test(name, count):
    while count > 0:
        # schedule what to do
        global num
        num += 1
        count -= 1
        # print message
        print(name + ' test one time.')
        # sleep one second
        time.sleep(1)
# Create thread
t = threading.Thread(target=test, args=('No.1 thread ', 5))
# Set thread to daemon
t.setDaemon(True)
# Create thread
t1 = threading.Thread(target=test, args=('No.2 thread ', 5))
# Set thread to daemon
t1.setDaemon(True)
# Start thread to execute
t.start()
t1.start()
print('Start Thread')
t.join()
'''
t -> False
t1 -> True
这个时候就会自动将t1线程设置为t线程的守护线程
'''

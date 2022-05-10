import threading
# Test threading daemon.
def createThread():
    print('Starting thread.')
    i = 0
    while True:
        print('Heartbeat {}'.format(i))
        i += 1
        time.sleep(1)



thread = threading.Thread(target=createThread)


# Set to false to kill thread after test.
thread.setDaemon(False)

thread.start()

print('Started thread.')

for i in range(0, 10):
    print('Test value {}'.format(i))
    time.sleep(1)

print('Exiting thread.')
</code>


import sys, threading

def run():
    i = 0
    while True:
        i+=1

thread = threading.Thread(target=run)
thread.setDaemon(True)
thread.start()

while thread.isAlive():
    print('still running...')
    time.sleep(1)

print('thread ended')
print('program ended')
</code>
Output:
<code>still running...
still running...
still running...
still running...
still running...
still running...
still running...
still running...
thread ended
program ended
</code>


import sys, threading

def run():
    while True:
        print('thread running')
        time.sleep(1)

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

print('main thread')

while True:
    time.sleep(1)
    print('main thread running')
</code>
The output is:
<code>main thread
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running
thread running
main thread running


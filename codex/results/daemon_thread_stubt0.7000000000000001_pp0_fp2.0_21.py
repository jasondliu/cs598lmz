import sys, threading

def run():
    while True:
        print('thread running')
        time.sleep(1)

threading.Thread(target=run).start()
print('main thread')

while True:
    pass
</code>
I want the program to print 'main thread' once, then print 'thread running' every second. Instead, it prints 'main thread' every second. How can I fix this?


import sys, threading

def run():
    sys.stdin = open('/dev/tty')
    print('Welcome. Type exit to quit.')
    while True:
        print('>', end=' ')
        line = sys.stdin.readline().rstrip('\r\n')
        if line == 'exit':
            break

threading.Thread(target=run).start()

while True:
    time.sleep(1)
```

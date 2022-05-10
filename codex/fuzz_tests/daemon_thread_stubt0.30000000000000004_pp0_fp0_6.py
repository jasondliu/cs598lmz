import sys, threading

def run():
    for i in range(10):
        print(i)
        time.sleep(0.1)

t = threading.Thread(target=run)
t.start()

while True:
    try:
        sys.stdin.read()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        break
</code>


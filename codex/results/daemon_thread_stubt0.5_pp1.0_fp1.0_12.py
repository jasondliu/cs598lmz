import sys, threading

def run():
    for i in range(5):
        print(i)
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    print('main thread')
    time.sleep(1)
    if not t.is_alive():
        break

print('end')
</code>


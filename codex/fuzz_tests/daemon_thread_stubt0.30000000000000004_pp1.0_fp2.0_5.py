import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)

t = threading.Thread(target=run)
t.start()

for i in range(10):
    print(i)
    time.sleep(1)

t.join()
print('done')

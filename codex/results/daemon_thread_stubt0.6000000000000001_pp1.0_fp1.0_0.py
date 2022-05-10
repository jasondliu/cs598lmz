import sys, threading

def run():
    for i in range(10):
        sys.stdout.write('{}\n'.format(i))
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    line = sys.stdin.readline()
    if line.strip() == 'exit':
        break
    print(line)

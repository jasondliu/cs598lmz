import sys, threading

def run():
    sys.stdout.write('hello\n')
    time.sleep(2)
    sys.stdout.write('world\n')

thr = threading.Thread(target=run)
thr.start()
thr.join()
print('thread end')

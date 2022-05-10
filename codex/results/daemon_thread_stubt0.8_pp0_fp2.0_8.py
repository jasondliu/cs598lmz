import sys, threading

def run():
    sys.stdout.write('Thread %s\n' % threading.current_thread().getName())
    sys.stdout.flush()

th=threading.Thread(target=run, name='Worker')
th.start()

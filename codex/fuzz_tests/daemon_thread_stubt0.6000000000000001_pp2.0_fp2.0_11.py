import sys, threading

def run():
    sys.stdout.write('Thread\n')

t = threading.Thread(target=run)
t.start()
sys.stdout.write('Main\n')

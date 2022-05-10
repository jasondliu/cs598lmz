import sys, threading

def run():
    for i in range(10):
        sys.stdout.write('Hello from thread %s\n' % threading.currentThread())

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()

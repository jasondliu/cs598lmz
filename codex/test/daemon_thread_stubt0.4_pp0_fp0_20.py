import sys, threading

def run():
    sys.stdout.write('Hello from thread %s\n' % threading.currentThread())

def test():
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()

if __name__ == "__main__":
    test()

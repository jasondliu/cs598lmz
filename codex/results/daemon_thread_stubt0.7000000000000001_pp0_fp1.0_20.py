import sys, threading

def run():
    with open('/tmp/a.txt', 'w') as f:
        f.write(str(os.getpid()))
    while True:
        pass

if __name__ == '__main__':
    run()

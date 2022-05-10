import sys, threading

def run():
    for i in range(0, 100):
        print i
        time.sleep(1)

if __name__ == '__main__':
    run()
    sys.exit(0)

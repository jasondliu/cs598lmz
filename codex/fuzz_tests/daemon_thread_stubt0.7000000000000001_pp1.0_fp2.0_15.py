import sys, threading

def run():
    print 'Hello from thread'

def main():
    for i in range(5):
        th = threading.Thread(target=run)
        th.start()

if __name__ == '__main__':
    main()

import sys, threading

def run():
    Lock = threading.Lock()
    while True:
        Lock.acquire()
        with open(str(sys.argv[1]), 'r') as f:
            data = f.read()
            print(data)
        Lock.release()
    
if __name__ == '__main__':
    run()

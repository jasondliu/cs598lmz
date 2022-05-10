import threading
# Test threading daemon, it's not good for this.
def myThread(id):
    print("This is thread %d" % id)

def main():
    for i in range(0, 2):
        t = threading.Thread(target=myThread, args=(i,))
        #t.daemon = True
        t.start()

if __name__ == '__main__':
    main()


import threading
# Test threading daemon, it's not good for this.
def myThread(id):
    print("This is thread %d" % id)

def main():
    for i in range(0, 2):
        t = threading.Thread(target=myThread, args=(i,))
        #t.daemon = True
        t.start()

if __name__ == '__main__':
    main()

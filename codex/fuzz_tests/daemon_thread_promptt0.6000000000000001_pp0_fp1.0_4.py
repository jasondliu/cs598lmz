import threading
# Test threading daemon
def myThread(id):
    print("thread-" + str(id) + " start")
    time.sleep(10)
    print("thread-" + str(id) + " stop")

def main():
    for i in range(4):
        t = threading.Thread(target=myThread, args=(i,))
        t.setDaemon(True)
        t.start()
    t.join()
    print("main thread stop")

if __name__ == '__main__':
    main()

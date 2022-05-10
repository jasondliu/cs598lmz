import threading
# Test threading daemon
def func():
    while 1:
        time.sleep(2)
        print("sleep 2s")
t = threading.Thread(target = func)
t.setDaemon(True)
t.start()

def main():
    print("i'm main, start")
    time.sleep(1)
    print("i'm main, stop")

if __name__ == '__main__':
    main()

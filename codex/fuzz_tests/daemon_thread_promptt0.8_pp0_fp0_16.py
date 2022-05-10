import threading
# Test threading daemon.

def print_thread():
    i = 0
    while(True):
        print(i)
        time.sleep(0.5)
        i += 1

def main():
    print('In main')
    thread = threading.Thread(target = print_thread)
    thread.setDaemon(False)
    thread.start()
    thread.join()
    print('Thread finished')


if __name__ == "__main__":
    main()

import threading
# Test threading daemon
def main():
    print("Main Thread: ", threading.current_thread().name)
    for i in range(2):
        t = threading.Thread(target=daemon, name="Daemon Thread: {}".format(i+1))
        t.setDaemon(True)
        t.start()
        t.join()

def daemon():
    print("Daemon Thread: ", threading.current_thread().name)
    time.sleep(1)
    print("Daemon Thread: ", threading.current_thread().name)

if __name__ == '__main__':
    main()

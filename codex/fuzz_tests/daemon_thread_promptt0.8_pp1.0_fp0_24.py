import threading
# Test threading daemon
def test():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')
# Main Thread
def main():
    for i in range(3):
        t = threading.Thread(name = f'Child Thread {i}', target = test)
        t.setDaemon(True)  # Set Thread Daemon
        t.start()
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(1)
    print(threading.currentThread().getName(), 'Exiting')
# Main Thread Daemon
if __name__ == '__main__':
    main()
    print('End of Program')

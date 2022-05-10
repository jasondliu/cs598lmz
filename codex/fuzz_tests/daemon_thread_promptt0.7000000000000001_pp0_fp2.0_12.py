import threading
# Test threading daemon thread
def func1():
    while True:
        print ('func1')

def func2():
    while True:
        print ('func2')

def main():
    # Create thread with func1 
    th1 = threading.Thread(target=func1)
    # Create thread with func1 
    th2 = threading.Thread(target=func2)

    # Set daemon thread
    th1.setDaemon(True)
    th2.setDaemon(True)

    # Start thread
    th1.start()
    th2.start()

    # Waiting for thread terminated
    th1.join()
    th2.join()

if __name__ == '__main__':
    main()

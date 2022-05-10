import threading
# Test threading daemon
import time

def thread_function():
    print("Thread function")
    time.sleep(10)
    print("Thread function after sleep")

def main():
    print("Main function")
    t1 = threading.Thread(target=thread_function)
    t1.daemon = True
    t1.start()
    print("Main function after thread start")
    time.sleep(5)
    print("Main function after sleep")

if __name__ == "__main__":
    main()

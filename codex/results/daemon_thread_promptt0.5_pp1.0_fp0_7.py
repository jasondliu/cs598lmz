import threading
# Test threading daemon
import time

def my_func():
    print("Hello world")

def main():
    t = threading.Thread(target=my_func)
    t.setDaemon(True)
    t.start()

    print("Hello world")
    time.sleep(1)


if __name__ == "__main__":
    main()

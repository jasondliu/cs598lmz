import threading
# Test threading daemon
import time

def main():
    print("Main start")
    t = threading.Thread(target=thread_func)
    t.setDaemon(True)
    t.start()
    time.sleep(1)
    print("Main end")

def thread_func():
    print("Thread start")
    time.sleep(5)
    print("Thread end")

if __name__ == "__main__":
    main()

# Main start
# Thread start
# Main end

# 이렇게 되면, main이 끝나면 thread_func도 종료된다.

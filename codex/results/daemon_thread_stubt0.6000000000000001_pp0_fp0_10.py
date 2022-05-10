import sys, threading

def run():
    print("Hello from other thread.")

    print("Threads name: ", threading.currentThread().getName())
    print("Threads name: ", threading.current_thread().getName())

if __name__ == "__main__":
    print("Hello from main thread.")
    print("Threads name: ", threading.currentThread().getName())
    print("Threads name: ", threading.current_thread().getName())

    t = threading.Thread(target=run)
    t.start()

    name_threads = threading.enumerate()
    print("Total threads:", len(name_threads))

    for name_thread in name_threads:
        print("Thread: ", name_thread)

    for t in threading.enumerate():
        print("Thread: ", t)

# Result:
# Hello from main thread.
# Threads name:  MainThread
# Threads name:  MainThread
# Hello from other thread.
# Threads name:  Thread-1
# Threads name:  Thread-1
# Total

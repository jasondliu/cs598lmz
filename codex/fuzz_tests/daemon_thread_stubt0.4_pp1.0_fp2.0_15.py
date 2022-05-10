import sys, threading

def run():
    print("Thread", threading.current_thread().getName(), "started")
    while True:
        pass

def main():
    print("Thread", threading.current_thread().getName(), "started")
    for i in range(5):
        threading.Thread(target=run, name="Thread-{}".format(i+1)).start()
    print("Thread", threading.current_thread().getName(), "finished")

if __name__ == "__main__":
    main()
</code>


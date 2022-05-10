import sys, threading

def run():
    while True:
        print(threading.current_thread().name, end="")
        sys.stdout.flush()

def main():
    threading.Thread(target=run, name="thread1").start()
    threading.Thread(target=run, name="thread2").start()
    run()

if __name__ == "__main__":
    main()

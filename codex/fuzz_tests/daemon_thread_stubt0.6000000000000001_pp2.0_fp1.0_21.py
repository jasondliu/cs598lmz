import sys, threading

def run():
    print("hello from thread %s\n" % threading.current_thread().name)

def main():
    print("Hello from thread %s\n" % threading.current_thread().name)
    t = threading.Thread(target=run, name="MyThread")
    t.start()

if __name__ == "__main__":
    main()

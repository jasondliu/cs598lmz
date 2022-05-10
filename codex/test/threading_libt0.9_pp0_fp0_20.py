import threading
threading.stack_size(32768)

def job():
    print("thread %s is running" % threading.current_thread())

def main():
    print("thread %s is running" % threading.current_thread())
    for i in range(2):
        t = threading.Thread(target=job)
        t.start()

if __name__ == "__main__":
    main()

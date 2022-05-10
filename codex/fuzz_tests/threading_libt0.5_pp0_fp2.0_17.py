import threading
threading.stack_size(67108864)

def main():
    print("main thread started")
    t = threading.Thread(target=f, args=(1,))
    t.start()
    t.join()
    print("main thread ended")

def f(i):
    print("thread started")
    for x in range(10):
        print(i, ":", x)
    print("thread ended")

if __name__ == "__main__":
    main()

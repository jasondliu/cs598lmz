import sys, threading

def run():
    n = 10
    for i in range(n):
        print(threading.current_thread().name + ": " + str(i))
    print("Done")

def main():
    print("Main thread")
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("Main thread finished")

if __name__ == "__main__":
    main()

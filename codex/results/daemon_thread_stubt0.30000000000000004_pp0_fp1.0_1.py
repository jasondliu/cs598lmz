import sys, threading

def run():
    while True:
        print("Thread")
        time.sleep(1)

def main():
    print("Main")
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print("Main end")

if __name__ == "__main__":
    main()

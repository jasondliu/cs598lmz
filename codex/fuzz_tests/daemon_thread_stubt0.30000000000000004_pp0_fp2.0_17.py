import sys, threading

def run():
    print("starting")
    time.sleep(2)
    print("Exiting")

def main():
    t = threading.Thread(target=run)
    t.start()
    print("Waiting for thread to complete")
    t.join()
    print("Thread completed")

if __name__ == "__main__":
    main()

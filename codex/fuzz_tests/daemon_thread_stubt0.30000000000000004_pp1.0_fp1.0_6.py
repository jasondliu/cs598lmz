import sys, threading

def run():
    for i in range(10):
        print(i)
        time.sleep(0.1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()

if __name__ == "__main__":
    main()

import sys, threading

def run():
    while True:
        print("hello")
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    time.sleep(10)

if __name__ == "__main__":
    main()
</code>


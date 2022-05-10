import sys, threading

def run():
    while True:
        print("Hello World")
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()

if __name__ == "__main__":
    main()
</code>


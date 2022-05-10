import sys, threading

def run():
    x = 0
    while True:
        try:
            x += 1
        except KeyboardInterrupt:
            print("Interrupted by user")
            return

def main():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    thread.join()

if __name__ == "__main__":
    main()
</code>


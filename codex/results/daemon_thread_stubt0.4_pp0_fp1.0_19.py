import sys, threading

def run():
    print("Running")
    time.sleep(10)
    print("Done")

def main():
    print("Main")
    threading.Thread(target=run).start()
    print("Main Done")

if __name__ == "__main__":
    main()

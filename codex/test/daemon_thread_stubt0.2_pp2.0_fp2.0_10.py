import sys, threading

def run():
    print("I'm a thread")

def main():
    t = threading.Thread(target=run)
    t.start()
    print("I'm a main thread")

if __name__ == "__main__":
    main()

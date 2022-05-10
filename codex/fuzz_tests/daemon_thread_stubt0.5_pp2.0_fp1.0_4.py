import sys, threading

def run():
    print("Hello from new thread")

def main():
    print("Hello from main thread")
    t = threading.Thread(target=run)
    t.start()
    print("Hello again from main thread")

if __name__ == "__main__":
    main()

# threading.Thread(target=run)
# t.start()
# t.join()
# print("Hello again from main thread")

# t = threading.Thread(target=run)
# t.start()
# t.join()
# print("Hello again from main thread")

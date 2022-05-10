import sys, threading

def run():
    for i in range(10):
        print("Hello")

def main():
    t = threading.Thread(target=run)
    t.start()
    t.join()

if __name__ == "__main__":
    main()

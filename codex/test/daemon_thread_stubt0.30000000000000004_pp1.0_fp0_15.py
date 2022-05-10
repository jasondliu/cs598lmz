import sys, threading

def run():
    while True:
        print("Hello")

def main():
    t = threading.Thread(target=run)
    t.start()

if __name__ == "__main__":
    main()

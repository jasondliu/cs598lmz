import sys, threading

def run():
    for i in range(1, 10):
        print(i)
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()

    while True:
        print("Hello")
        time.sleep(1)

if __name__ == "__main__":
    main()

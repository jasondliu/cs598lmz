import sys, threading

def run():
    print("run")

def main():
    threads = []

    for i in range(5):
        t = threading.Thread(target=run)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()

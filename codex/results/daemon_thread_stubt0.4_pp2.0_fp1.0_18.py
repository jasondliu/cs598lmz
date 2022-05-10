import sys, threading

def run():
    print("run")
    time.sleep(1)

def main():
    for i in range(10):
        threading.Thread(target=run).start()

if __name__ == '__main__':
    main()

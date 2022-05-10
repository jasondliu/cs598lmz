import sys, threading

def run():
    for i in range(100):
        print("run")

def main():
    t = threading.Thread(target=run)
    t.start()
    for i in range(100):
        print("main")

if __name__ == '__main__':
    main()

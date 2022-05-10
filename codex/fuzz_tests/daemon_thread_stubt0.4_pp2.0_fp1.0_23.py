import sys, threading

def run():
    while True:
        pass

if __name__ == "__main__":
    for i in range(int(sys.argv[1])):
        threading.Thread(target=run).start()

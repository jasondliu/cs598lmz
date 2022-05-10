import sys, threading

def run():
    while True:
        print("thread")

def main():
    i = 0
    while True:
        print("main")
        i += 1

        if i == 10:
            break

t = threading.Thread(target=run)
t.start()
main()

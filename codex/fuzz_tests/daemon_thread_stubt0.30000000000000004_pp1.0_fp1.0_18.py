import sys, threading

def run():
    print("Thread started")
    for i in range(0, 100):
        print(i)
    print("Thread finished")

def main():
    print("Main started")
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
    print("Main finished")

main()

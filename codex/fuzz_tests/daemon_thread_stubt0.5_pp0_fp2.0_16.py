import sys, threading

def run():
    print("Thread started")
    for i in range(0, 100):
        print(i)
        time.sleep(0.5)
    print("Thread finished")

thread = threading.Thread(target=run)
thread.start()

input("Enter to stop")

sys.exit()

import sys, threading

def run():
    while True:
        print("threading is running")
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()

    print("main threading")
    time.sleep(3)
    print("end")


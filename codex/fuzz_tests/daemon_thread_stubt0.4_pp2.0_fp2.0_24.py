import sys, threading

def run():
    while True:
        print("test")
        time.sleep(1)

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    while True:
        pass

import threading
# Test threading daemon

def test():
    while True:
        print("test")
        time.sleep(1)

def main():
    thread = threading.Thread(target=test)
    thread.setDaemon(True)
    thread.start()

    while True:
        print("main")
        time.sleep(1)

if __name__ == "__main__":
    main()

import threading
# Test threading daemon
def test():
    print("test")
    time.sleep(1)

def main():
    for i in range(5):
        t = threading.Thread(target=test)
        t.setDaemon(True)
        t.start()
    print("main")

if __name__ == "__main__":
    main()

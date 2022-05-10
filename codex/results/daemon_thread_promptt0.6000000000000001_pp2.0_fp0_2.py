import threading
# Test threading daemon

def test_daemon():
    print("Test daemon")
    time.sleep(2)
    print("Exit test daemon")

def test_non_daemon():
    print("Test non daemon")
    time.sleep(2)
    print("Exit test non daemon")

def main():
    t1 = threading.Thread(target=test_daemon)
    t2 = threading.Thread(target=test_non_daemon)
    
    t1.daemon = True
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()

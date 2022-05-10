import threading
# Test threading daemon
def test():
    while True:
        print("H")
        time.sleep(2)

t = threading.Thread(target=test)
t.setDaemon(True)
t.start()
time.sleep(10)
print("END")

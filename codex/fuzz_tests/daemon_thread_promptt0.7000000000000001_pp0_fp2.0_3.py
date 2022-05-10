import threading
# Test threading daemon


def target():
    while True:
        print("New thread")
        time.sleep(1)


thread = threading.Thread(target=target, args=(), daemon=True)

try:
    thread.start()
    time.sleep(10)
except KeyboardInterrupt:
    print("Finished")

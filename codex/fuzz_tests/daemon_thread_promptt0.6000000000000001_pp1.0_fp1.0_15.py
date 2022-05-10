import threading
# Test threading daemon

def run():
    while True:
        print("Threading running")
        time.sleep(1)


if __name__ == '__main__':
    t = threading.Thread(target=run, daemon=True)
    t.start()
    t.join()

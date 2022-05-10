import threading
# Test threading daemon

def run():
    print('start run')
    time.sleep(3)
    print('end run')

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

print('main thread')

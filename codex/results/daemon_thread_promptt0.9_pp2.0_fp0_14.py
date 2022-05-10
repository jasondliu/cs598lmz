import threading
# Test threading daemon

sleep_us=1000000
interval=1.0/sleep_us
key=9
i=0

def test_daemon():
    global i
    time.sleep(interval)
    i += 1
    print i

a = threading.Thread(target=test_daemon)
a.daemon=True
a.start()

while 1:
    key = raw_input('press 9 to exit')
    print key
    if key=='9':
        break

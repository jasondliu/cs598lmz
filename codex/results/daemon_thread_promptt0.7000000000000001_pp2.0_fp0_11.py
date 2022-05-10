import threading
# Test threading daemon

def wide_time():
    while True:
        time.sleep(1)
        print(time.ctime())

t = threading.Thread(target=wide_time)
t.setDaemon(True)
t.start()

print('Start Wide Time')

while True:
    time.sleep(1)
    print(time.ctime())

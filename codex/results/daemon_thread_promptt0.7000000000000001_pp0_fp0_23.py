import threading
# Test threading daemon
# import pdb; pdb.set_trace()
def run():
    while True:
        print('Hello')
        time.sleep(0.5)
t = threading.Thread(target=run)
t.setDaemon(True)
t.start()
time.sleep(1)
print('Test end.')

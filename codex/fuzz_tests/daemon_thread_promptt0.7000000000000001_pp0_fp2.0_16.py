import threading
# Test threading daemon


def daemon():
    print('start daemon')
    time.sleep(1)
    print('end daemon')


d = threading.Thread(target=daemon)
d.setDaemon(True)
d.start()

d.join()

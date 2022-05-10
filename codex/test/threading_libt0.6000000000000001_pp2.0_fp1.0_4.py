import threading
threading.Thread(target=lambda: d.read_loop()).start()
for i in range(20):
    time.sleep(0.1)
    d.write(b'a')

d.close()

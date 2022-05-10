import threading
threading.Thread(target=send).start()
time.sleep(50)
threading.Thread(target=receive).start()

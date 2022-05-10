import threading
threading.Thread(target=lambda:print(time.asctime())).start()


def t():
    print(time.asctime())
    threading.Timer(1,t).start()


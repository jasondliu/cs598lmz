import sys, threading

def run():
    global a
    while not a.isReady():
        a.onFrame()

if __name__ == "__main__":
    a = app.App(sys.argv)
    t = threading.Thread(target = run)
    t.daemon = True
    t.start()
    a.exec_()

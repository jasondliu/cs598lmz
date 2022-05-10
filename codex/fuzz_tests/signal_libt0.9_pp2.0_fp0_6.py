import signal
signal.signal(signal.SIGINT, lambda x,y: sys.exit(1))

def getScale():
    win = MyWidget()
    if not win.updateStatus():
        sys.exit()
    scale = win.getScale()
    if not scale:
        sys.exit()
    return scale

if __name__ == '__main__':
    print getScale()

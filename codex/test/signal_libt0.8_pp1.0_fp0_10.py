import signal
signal.signal(signal.SIGINT, handler)

while True:
    time.sleep(.2)
    print("foo")

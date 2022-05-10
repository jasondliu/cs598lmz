import signal
signal.signal(signal.SIGINT, handler)

def get_time():
    return int(round(time.time()*1000))


def read_data():
    while True:
        data = ser.readline()

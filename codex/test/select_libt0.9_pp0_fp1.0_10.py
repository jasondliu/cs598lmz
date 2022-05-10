import select
import serial

_EXIT = False

data = []

def data_received(c, data):
    if c in data:
        print(c, end="", flush=True)


def main():
    data_callback = lambda c: data_received(c, data)
    port = init_serial_port("COM20", 115200, timeout=1)
    r, _, _ = select.select([port], [], [])
    c = 0
    while not _EXIT:
        next(r, None)
        received = port.read()
        if received:
            if received.decode("utf-8") == "\r":
                data_callback("\n")
            else:
                data_callback(received.decode("utf-8"))
            sys.stdout.flush()



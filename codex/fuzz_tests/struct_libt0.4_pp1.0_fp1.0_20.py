import _struct
import datetime
import sys
import os
import time

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 {} <file>".format(sys.argv[0]))
        sys.exit(1)

    file = sys.argv[1]
    if not os.path.exists(file):
        print("File {} does not exist".format(file))
        sys.exit(1)

    with open(file, "rb") as f:
        f.seek(0x1C)
        start_time = _struct.unpack("<I", f.read(4))[0]
        f.seek(0x20)
        end_time = _struct.unpack("<I", f.read(4))[0]

        start = datetime.datetime.fromtimestamp(start_time)
        end = datetime.datetime.fromtimestamp(end_time)
        print("Start: {}".format(start.strftime("%Y-%m-%d %H:%M:

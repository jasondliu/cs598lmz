import _struct
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 {} <file>".format(sys.argv[0]))
        sys.exit(1)

    with open(sys.argv[1], "rb") as f:
        data = f.read()

    # check header
    if data[0:4] != b"\x00\x00\x00\x00":
        print("Invalid header")
        sys.exit(1)

    # read number of entries
    num_entries = _struct.unpack("<I", data[4:8])[0]
    print("Number of entries: {}".format(num_entries))

    # read entries
    entries = []
    for i in range(num_entries):
        offset = 8 + (i * 0x10)
        entry = {
            "hash": _struct.unpack("<I", data[offset:offset+4])[0],
            "offset": _struct.unpack("<I", data[offset+

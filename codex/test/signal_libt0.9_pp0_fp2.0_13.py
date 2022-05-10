import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

import sys
import struct
import socket
import telnetlib
import hexdump

HOST, PORT = "ctf.hackucf.org", 20005

def read(fmt, f):
    raw = f.read(struct.calcsize(fmt))
    return struct.unpack(fmt, raw)

def readline(f):
    bytes = f.readline().strip()
    return int.from_bytes(bytes, "big")

def write(fmt, f, value):
    f.write(struct.pack(fmt, value))


def addr(x):
    return struct.pack("<Q", x)

if len(sys.argv) < 2:
    print("Usage:", sys.argv[0], "<input>")
    print("Or:", sys.argv[0], "<input> -d")
    sys.exit(-1)

debug = (sys.argv[2] == "-d")


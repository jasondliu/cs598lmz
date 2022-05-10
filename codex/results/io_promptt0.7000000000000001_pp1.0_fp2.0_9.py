import io
# Test io.RawIOBase things

raw = io.RawIOBase()

try:
    raw.readinto(b"")
except io.UnsupportedOperation as e:
    print(e)

try:
    raw.readinto1(b"")
except io.UnsupportedOperation as e:
    print(e)

try:
    raw.readall()
except io.UnsupportedOperation as e:
    print(e)

try:
    raw.read1()
except io.UnsupportedOperation as e:
    print(e)

try:
    raw.readline()
except io.UnsupportedOperation as e:
    print(e)

try:
    raw.readlines()
except io.UnsupportedOperation as e:
    print(e)

try:
    raw.read(0)
except io.UnsupportedOperation as e:
    print(e)

try:
    raw.write(b"")
except io.UnsupportedOperation as e:
    print(e)

try:
    raw.seek(0)
except io.Unsupported

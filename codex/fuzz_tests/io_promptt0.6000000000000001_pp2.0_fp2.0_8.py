import io
# Test io.RawIOBase

print('io.RawIOBase')

raw = io.RawIOBase()

print('io.RawIOBase.read()')
try:
    raw.read()
except io.UnsupportedOperation:
    print('UnsupportedOperation')

print('io.RawIOBase.readinto()')
try:
    raw.readinto(bytearray(1))
except io.UnsupportedOperation:
    print('UnsupportedOperation')

print('io.RawIOBase.readall()')
try:
    raw.readall()
except io.UnsupportedOperation:
    print('UnsupportedOperation')

print('io.RawIOBase.readinto1()')
try:
    raw.readinto1(bytearray(1))
except io.UnsupportedOperation:
    print('UnsupportedOperation')

print('io.RawIOBase.readline()')
try:
    raw.readline()
except io.UnsupportedOperation:
    print('UnsupportedOperation')

print('io.RawIOBase.readlines()')
try:
    raw.

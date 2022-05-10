import io
# Test io.RawIOBase
raw = io.RawIOBase()
try:
    raw.read()
except NotImplementedError:
    print('read() not implemented')
raw.closed

raw.close()
raw.closed
# Test io.BufferedIOBase
buf = io.BufferedIOBase()
try:
    buf.read()
except NotImplementedError:
    print('read() not implemented')
buf.closed

buf.close()
buf.closed
# Test io.TextIOBase
txt = io.TextIOBase()
try:
    txt.read()
except NotImplementedError:
    print('read() not implemented')
txt.closed

txt.close()
txt.closed
txt.newlines
# io.StringIO is buffered by default
# Test io.IOBase
io = io.IOBase()
try:
    io.read()
except NotImplementedError:
    print('read() not implemented')
io.closed

io.close()
io.closed
# FileIO is the raw
from io import FileIO
try:
   

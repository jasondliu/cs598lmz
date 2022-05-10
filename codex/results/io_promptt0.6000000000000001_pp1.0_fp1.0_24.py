import io
# Test io.RawIOBase
rawio = io.RawIOBase()
try:
    rawio.read()
except NotImplementedError:
    pass
try:
    rawio.readinto()
except NotImplementedError:
    pass
try:
    rawio.write(b'')
except NotImplementedError:
    pass
try:
    rawio.seek(0)
except NotImplementedError:
    pass
try:
    rawio.tell()
except NotImplementedError:
    pass
try:
    rawio.truncate()
except NotImplementedError:
    pass
try:
    rawio.fileno()
except NotImplementedError:
    pass
try:
    rawio.isatty()
except NotImplementedError:
    pass
try:
    rawio.readable()
except NotImplementedError:
    pass
try:
    rawio.writable()
except NotImplementedError:
    pass
try:
    rawio.seekable()
except NotImplementedError:
    pass


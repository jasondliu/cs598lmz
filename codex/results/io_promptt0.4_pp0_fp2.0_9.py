import io
# Test io.RawIOBase
try:
    io.RawIOBase()
except TypeError:
    print('SKIP')
    raise SystemExit

# Test io.FileIO
try:
    io.FileIO()
except TypeError:
    print('SKIP')
    raise SystemExit

# Test io.BufferedIOBase
try:
    io.BufferedIOBase()
except TypeError:
    print('SKIP')
    raise SystemExit

# Test io.BytesIO
try:
    io.BytesIO()
except TypeError:
    print('SKIP')
    raise SystemExit

# Test io.StringIO
try:
    io.StringIO()
except TypeError:
    print('SKIP')
    raise SystemExit

# Test io.BufferedWriter
try:
    io.BufferedWriter()
except TypeError:
    print('SKIP')
    raise SystemExit

# Test io.BufferedReader
try:
    io.BufferedReader()
except TypeError:
    print('SKIP')
    raise SystemExit

# Test io.BufferedR

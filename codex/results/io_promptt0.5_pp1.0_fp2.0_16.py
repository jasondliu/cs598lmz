import io
# Test io.RawIOBase
try:
    io.RawIOBase.close
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test io.BufferedIOBase
try:
    io.BufferedIOBase.close
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test io.TextIOBase
try:
    io.TextIOBase.close
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test io.BytesIO
try:
    io.BytesIO
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test io.StringIO
try:
    io.StringIO
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test io.FileIO
try:
    io.FileIO
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test io.BufferedReader
try:
    io.BufferedReader
except AttributeError:
    print('SKIP')
    raise SystemExit

#

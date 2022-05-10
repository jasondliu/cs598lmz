import io
# Test io.RawIOBase
try:
    io.RawIOBase().readinto()
except AttributeError:
    pass
else:
    print("SKIP")
    raise SystemExit

# Test io.BufferedIOBase
try:
    io.BufferedIOBase().readinto()
except AttributeError:
    pass
else:
    print("SKIP")
    raise SystemExit

# Test io.RawIOBase
try:
    io.RawIOBase().readinto1()
except AttributeError:
    pass
else:
    print("SKIP")
    raise SystemExit

# Test io.BufferedIOBase
try:
    io.BufferedIOBase().readinto1()
except AttributeError:
    pass
else:
    print("SKIP")
    raise SystemExit

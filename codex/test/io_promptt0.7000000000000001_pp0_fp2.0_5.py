import io
# Test io.RawIOBase
with io.RawIOBase() as f:
    print(f"raw: {f}")
    print(f"isatty: {f.isatty()}")

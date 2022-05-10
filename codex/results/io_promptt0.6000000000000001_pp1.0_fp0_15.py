import io
# Test io.RawIOBase
buf = io.BytesIO()
buf.write(b'Hello')
buf.seek(0)
buf.read()

# Test io.BufferedIOBase
buf = io.BytesIO()
buf.write(b'Hello')
buf.seek(0)
buf.read()

# Test io.TextIOBase
buf = io.StringIO()
buf.write('Hello')
buf.seek(0)
buf.read()

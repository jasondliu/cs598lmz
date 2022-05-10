import io
# Test io.RawIOBase
fo = io.BytesIO()

print('File closed?', fo.closed)

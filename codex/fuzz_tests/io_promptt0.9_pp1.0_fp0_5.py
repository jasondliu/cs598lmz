import io
# Test io.RawIOBase
with io.RawIOBase() as stream:
  print("stream:", stream)
  print("stream.close():", stream.close())

assert stream.closed

# Test io.BytesIO
with io.BytesIO() as bytes_io:
  print("bytes_io:", bytes_io)
  # Seeks to the absolute byte position pos.
  print("bytes_io.seek(4):", bytes_io.seek(4))
  # Seeks relative to current position
  print("bytes_io.seek(4,1):", bytes_io.seek(4,1))

# Test io.StringIO
with io.StringIO() as string_io:
  print("string_io:", string_io)

# Test io.BufferedIOBase
with io.BufferedIOBase() as base_buffer:
  print("base_buffer:", base_buffer)
  print("base_buffer.getbuffer():", base_buffer.getbuffer())

# Test io.BufferedReader
with io.BufferedReader(io.BytesIO(b"abc")) as

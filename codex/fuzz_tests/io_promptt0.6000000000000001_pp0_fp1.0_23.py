import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.TextIOBase

# Test io.FileIO
with io.FileIO("input.txt", "w") as file:
    file.write(b"A\n")
    file.write(b"B\n")
    file.write(b"C\n")
    file.seek(0, 0)
    for line in file:
        print(line.strip())
    file.close()

# Test io.BytesIO
with io.BytesIO() as buffer:
    buffer.write(b"A\n")
    buffer.write(b"B\n")
    buffer.write(b"C\n")
    buffer.seek(0, 0)
    for line in buffer:
        print(line.strip())
    buffer.close()

# Test io.StringIO
with io.StringIO() as buffer:
    buffer.write("A\n")
    buffer.write("B\n")
    buffer.write("C\n")
    buffer.seek(0, 0)
    for

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

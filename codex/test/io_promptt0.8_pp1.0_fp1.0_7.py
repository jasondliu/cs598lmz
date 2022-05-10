import io
# Test io.RawIOBase with a raw string
with io.StringIO('Fnord') as x:
    for line in x.readlines():
        print(line)

# Test BufferedWriter with byte-mode io.StringIO

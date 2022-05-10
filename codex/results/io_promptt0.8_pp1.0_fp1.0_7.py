import io
# Test io.RawIOBase with a raw string
with io.StringIO('Fnord') as x:
    for line in x.readlines():
        print(line)

# Test BufferedWriter with byte-mode io.StringIO
with io.StringIO() as x:
    with io.BufferedWriter(x, 10000) as y:
        y.write('Fnord')
    print(x.getvalue())

# Test BufferedReader with text-mode io.StringIO
with io.StringIO('Fnord') as x:
    with io.BufferedReader(x, 10000) as y:
        for line in y.readlines():
            print(line)

# Test BufferedRandom with byte-mode io.StringIO
with io.StringIO() as x:
    with io.BufferedRandom(x, 10000) as y:
        y.write(b'Fnord')
    print(x.getvalue())

# Test BufferedRandom with text-mode io.StringIO
with io.StringIO('Fnord') as x:
    with io.BufferedRandom(

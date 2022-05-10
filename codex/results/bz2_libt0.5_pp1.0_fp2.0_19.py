import bz2
bz2.compress(b'hello world')

# compress file
bz2.compress(open('/etc/passwd', 'rb').read())

# compress file with context manager
with bz2.BZ2File('/tmp/example.bz2', 'w') as output:
    with open('/etc/passwd', 'rb') as input:
        output.writelines(input)

# compress file with context manager
with open('/etc/passwd', 'rb') as input:
    data = bz2.compress(input.read())

# compress file with context manager
with open('/etc/passwd', 'rb') as input:
    with bz2.BZ2File('/tmp/example.bz2', 'w') as output:
        output.writelines(input)

# compress file with context manager
with open('/etc/passwd', 'rb') as input:
    with bz2.BZ2File('/tmp/example.bz2', 'w') as output:
        for line in input:
            output

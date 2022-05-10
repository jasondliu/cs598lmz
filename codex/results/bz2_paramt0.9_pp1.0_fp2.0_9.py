from bz2 import BZ2Decompressor
BZ2Decompressor

if not use_stdin:
    if len(args) == 0 or args == ['-']:
        args = ['-']
    for fn in args:
        if fn == '-':
            fh = sys.stdin
        else:
            fh = open(fn, 'rb')
        decompressor = BZ2Decompressor()
        while True:
            input = fh.read(1024)
            if not input:
                break
            output = decompressor.decompress(input)
            if output:
                sys.stdout.write(output)
        if fn != '-':
            fh.close()
else:
    decompressor = BZ2Decompressor()
    while True:
        input = sys.stdin.read(1024)
        if not input:
            break
        output = decompressor.decompress(input)
        if output:
            sys.stdout.write(output)

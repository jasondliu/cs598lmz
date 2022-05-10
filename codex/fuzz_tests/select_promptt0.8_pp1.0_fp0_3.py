import select
# Test select.select()
def selectpoll():
    """selectpoll() - Use select() to monitor a pair of pipes."""
    pipe1r, pipe1w = os.pipe()
    pipe2r, pipe2w = os.pipe()
    readpipe, writepipe = (pipe1r, pipe2w)
    print 'pipes are:', pipe1r, pipe1w, pipe2r, pipe2w
    print 'starting select()'
    while True:
        readx, writex, exceptx = select.select([readpipe], [writepipe], [])
        if readx:
            print 'got input from pipe', readpipe, '- reading a line'
            line = os.read(readpipe, 500)
            print 'input from pipe', readpipe, 'is', `line`
            print 'swapping pipes'
            readpipe, writepipe = writepipe, readpipe
            print 'input on', readpipe, 'output on', writepipe
        if writex:
            print 'sending output to pipe', writepipe
            os.write(writepipe,

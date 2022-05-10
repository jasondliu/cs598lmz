import select
# Test select.select()
def selectpoll():
    """selectpoll() - Use select() to monitor a pair of pipes."""
    pipe1r, pipe1w = os.pipe()
    pipe2r, pipe2w = os.pipe()
    readpipe, writepipe = (pipe1r, pipe2w)

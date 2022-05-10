import io
# Test io.RawIOBase subclasses.

# Some helper functions

def check_io(io, expected):
    while True:
        s = io.read(1)
        if not s:
            break
        assert s == expected

def check_io_chunks(io, expected):
    while True:
        s = io.read(2)
        if not s:
            break
        assert s == expected

def check_io_peek(io, expected):
    while True:
        peeked = io.peek(100)
        assert peeked == expected
        s = io.read(1)
        if not s:
            break
        assert s == expected

def check_io_readall(io, expected):
    assert io.readall() == expected

def check_io_readline(io, expected):
    while True:
        s = io.readline(24)
        if not s:
            break
        assert s == expected

def check_io_readlines(io, expected):
    assert io.readlines() == expected

def check_

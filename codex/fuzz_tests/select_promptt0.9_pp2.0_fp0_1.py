import select
# Test select.select
typelist = [select.PIPE, select.PIPE, select.PIPE]
fdlist = typelist[:]
print typelist, fdlist
assert typelist == fdlist

for typename in 'PIPE', 'FIFO', 'SOCKET', 'FILE', 'TERMIOS', 'TTY', 'TTYS', 'IO':
    print typename

for typename in 'PIPE', 'FIFO', 'SOCKET', 'FILE', 'TERMIOS', 'TTY', 'TTYS', 'IO':
    assert hasattr(select, typename), typename

for typename in 'PIPE', 'FIFO', 'SOCKET', 'FILE', 'TERMIOS', 'TTY', 'TTYS', 'IO':
    hasattr(select, typename)

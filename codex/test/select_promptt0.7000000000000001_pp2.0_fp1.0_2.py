import select
# Test select.select
select.select([],[],[],0)

# import pty
# Test pty.openpty
master, slave = pty.openpty()
os.close(master)
os.close(slave)

# import termios
# Test termios.tcflush
fd = os.open('/dev/tty', os.O_RDWR)
termios.tcflush(fd, termios.TCIFLUSH)
os.close(fd)

# import tty
# Test tty.setcbreak
fd = os.open('/dev/tty', os.O_RDWR)
tty.setcbreak(fd)
os.close(fd)

# Test tty.setraw
fd = os.open('/dev/tty', os.O_RDWR)
tty.setraw(fd)
os.close(fd)

# import curses
# Test curses.tigetnum
curses.tigetnum('colors')

# import curses
# Test curses.tparm

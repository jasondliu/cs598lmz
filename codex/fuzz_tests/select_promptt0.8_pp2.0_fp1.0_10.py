import select
# Test select.select
with open('/dev/tty', 'rb') as tty:
    while True:
        # if there's data in the input buffer of tty,
        # 0.5s later, select will return the fd of tty
        if select.select([tty], [], []) == ([tty], [], []):
            # read a char
            char = tty.read(1)
            # print it out
            print(char)

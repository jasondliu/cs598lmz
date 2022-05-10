import select
# Test select.select() using stdin

read_list = [sys.stdin]
write_list = []
except_list = []

while True:
    read, write, except_ = select.select(read_list, write_list, except_list)
    for r in read:
        c = r.read(1)
        if c == 'q':
            sys.exit()
        sys.stdout.write(c)

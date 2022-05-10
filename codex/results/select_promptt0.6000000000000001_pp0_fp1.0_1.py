import select
# Test select.select()

read_list = [sys.stdin]
write_list = []
error_list = [sys.stderr]

while True:
    read, write, error = select.select(read_list, write_list, error_list)

    for s in read:
        line = s.readline()
        print("Read:", line)

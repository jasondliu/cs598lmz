import select
# Test select.select

read_list = []
write_list = []
except_list = []

while True:
    read_list, write_list, except_list = select.select(read_list, write_list, except_list)
    print('read_list:', read_list)
    print('write_list:', write_list)
    print('except_list:', except_list)
    time.sleep(2)

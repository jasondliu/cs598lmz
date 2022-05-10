import select
# Test select.select()
read_list = [sys.stdin]
print('Please input something: ')
readable, _, _ = select.select(read_list, [], [], 1000)
if readable:
    print(sys.stdin.readline())
else:
    print('Time out')

# 扩展
# select.poll()
# select.epoll()

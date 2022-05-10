import select
# Test select.select()

print('Entering blocking mode')
readable, writable, exceptional = select.select([sys.stdin], [], [])
print('Leaving blocking mode')

if not (readable or writable or exceptional):
    print('Time out')
else:
    print('Ready:', readable, writable, exceptional)

# 这个示例是非阻塞的，没有可读写的文件描述符，超时时间为0.0，也就是说只检查一下文件描述符，然后立即返回，不会阻塞等待。
# 这个示例是阻塞的，等待有可读写的文件描述符

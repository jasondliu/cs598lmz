import socket
socket.if_indextoname(5)
#'en8'
# and now pass only number to a url

with open('/tmp/test.txt', 'w') as to_delete:
    print(to_delete.name)
    to_delete.write('some')

os.lchmod(
    '/tmp/test.txt',
    stat.S_IRUSR|stat.S_IWUSR|
    stat.S_IRGRP|stat.S_IWGRP|
    stat.S_IROTH|stat.S_IWOTH,
)
# symlink:
os.lchmod('/tmp/test.txt', 0o666)
# file:
os.chmod('/tmp/test.txt', 0o666)

os.lchmod('/tmp/test.txt', stat.S_IREAD|stat.S_IWRITE)

os.lchmod('/tmp/test.txt', 0o666)

# open with symlink to file:
with open('/tmp/test.txt', buffering=0, encoding=

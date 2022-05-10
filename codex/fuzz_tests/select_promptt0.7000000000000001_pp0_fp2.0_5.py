import select
# Test select.select()

print("I'm running")

# 添加监听
fds = {}
fds[sys.stdin.fileno()] = sys.stdin
fds[sys.stdout.fileno()] = sys.stdout

while fds:
    # 调用select，监听所有的file descriptor
    # select.select(rlist, wlist, xlist[, timeout])
    # rlist：监听读事件列表；
    # wlist：监听写事件列表；
    # xlist：监听异常事件列表；
    # timeout：超时时间，None无限等待，0立即返回，>0超时时间
    readlist, writelist, xlist = select.select

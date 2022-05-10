import select
# Test select.select()

print("I'm running")

# 添加监听
fds = {}
fds[sys.stdin.fileno()] = sys.stdin

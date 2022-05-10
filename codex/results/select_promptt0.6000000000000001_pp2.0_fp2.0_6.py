import select
# Test select.select()

fd_list = []
fd_list.append(sys.stdin.fileno())

print("Before select.select()")
print("fd_list = ", fd_list)

print("After select.select()")
print("fd_list = ", fd_list)

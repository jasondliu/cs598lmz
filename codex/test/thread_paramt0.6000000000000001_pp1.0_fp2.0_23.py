import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(str(x) for x in range(int(input()),-1,-1)))).start()

# in:
# 3
# out:
# 3
# 2
# 1
# 0

# in:
# 5
# out:
# 5
# 4
# 3
# 2
# 1
# 0

# in:
# 10
# out:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, f(*map(int, open(0).read().split()))))))\
    .start()

# 別解
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, f(*map(int, open(0).read().split()))))).start()

# 別解
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, f(*map(int, open(0).read().split()))))).start()


# # 別解
# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, f(*map(int, open(0).read().split()))))).start()

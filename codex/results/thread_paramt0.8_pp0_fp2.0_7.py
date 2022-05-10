import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n".join(map(str, [[".", x][x in input()] for x in range(10)])))).start()

# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write("\n".join(map(str, [[".", x][x in input()] for x in range(10)])))).start()

# # from collections import Counter
# # import sys, threading
# # threading.Thread(target=lambda: sys.stdout.write("\n".join(map(str, [[".", x][x in Counter(list(input().strip()))] for x in range(10)])))).start()

# import sys, threading
# threading.Thread(target=lambda: sys.stdout.write("\n".join(map(str, [[".", x][x in [input()[int(input())//3==x] for x in range(3)]][input()[int(input())//3==x] for x in range(3)]] for x in range(10)]

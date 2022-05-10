import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

# with open(sys.argv[1], 'rb') as f:
#     content = f.read()
#     print(content)

# with open(sys.argv[1], 'rb') as f:
#     print(f.read())

# with open(sys.argv[1], 'rb') as f:
#     for line in f:
#         print(line)

# with open(sys.argv[1], 'rb') as f:
#     print(f.readline())

# with open(sys.argv[1], 'rb') as f:
#     print(f.readlines())

# with open(sys.argv[1], 'rb') as f:
#     print(f.readline())
#     print(f.readline())

# with open(sys.argv[1], 'rb') as f:
#     print(f.read(1))
#     print(f.read(1))
#    

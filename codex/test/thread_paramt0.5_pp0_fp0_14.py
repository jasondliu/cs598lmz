import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(sorted(input().split(), key=lambda x: (-len(x), x))))).start()
# print('\n'.join(sorted(input().split(), key=lambda x: (-len(x), x))))
# print(*sorted(input().split(), key=lambda x: (-len(x), x)), sep='\n')

# print(*sorted(input().split(), key=lambda x: (-len(x), x)), sep='\n')
# print('\n'.join(sorted(input().split(), key=lambda x: (-len(x), x))))
# print('\n'.join(sorted(input().split(), key=lambda x: (-len(x), x))))
# print('\n'.join(sorted(input().split(), key=lambda x: (-len(x), x))))
# print('\n'.join(sorted(input().split(), key=lambda x: (-len(x), x))))
# print('\n'.join(sorted(input().split(), key=lambda x: (-len(

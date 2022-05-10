import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()


print('\n'.join(map(str, part1())))
open('result.txt', 'w').write(str(part2()))

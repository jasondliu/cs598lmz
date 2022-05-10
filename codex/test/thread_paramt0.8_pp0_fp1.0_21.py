import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000)) + ['STOP']))).start()

for line in iter(sys.stdin.readline, ''):
    print(line)
    if line.rstrip() == 'STOP':
        break

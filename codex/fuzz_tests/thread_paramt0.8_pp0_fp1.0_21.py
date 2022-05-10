import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, range(100000)) + ['STOP']))).start()

for line in iter(sys.stdin.readline, ''):
    print(line)
    if line.rstrip() == 'STOP':
        break
</code>

Note: <code>sys.stdout.write</code> must be used instead of <code>print</code> because print introduces unnecessary buffering which can make reading output difficult.

If your Python version is < 3.7, then ensure that <code>b'\n'</code> is passed as a final argument to <code>iter</code>.

Note: there is no need to import <code>sys</code> or <code>threading</code> in your main script, since you already import the <code>sys</code> and <code>threading</code> modules in your subprocess script.


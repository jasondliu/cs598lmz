import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join('{}..{}\n'.format(*x) for x in zip('a' * 6, 'b' * 6)))).start()
</code>


import sys, threading
threading.Thread(target=lambda:
                sys.stdout.write('\n'.join(sorted(sys.stdin.readlines())))).start()
</code>

<code>Y</code>: Why not use a lambda?  In Python, any function can be expressed as a lambda statement.


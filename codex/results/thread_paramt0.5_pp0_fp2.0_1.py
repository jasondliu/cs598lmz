import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32mHello World\x1b[0m\n')).start()

# Python 2.x only
import sys
sys.stdout.write('\x1b[1;32mHello World\x1b[0m\n')

# Python 2.x only
import sys
print >> sys.stderr, '\x1b[1;32mHello World\x1b[0m\n'

# Python 2.x only
import sys
print '\x1b[1;32mHello World\x1b[0m\n'

# Python 2.x only
import sys
print '\x1b[1;32mHello World\x1b[0m\n',

# Python 2.x only
import sys
print '\x1b[1;32mHello World\x1b[0m\n',

# Python 2.x only
import sys
print '\x1b[1;32mHello World\x1b[0m\n',



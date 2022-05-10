import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(sys.argv[1:]))).start()
"""

#
# The following is a simple example of a script that can be run from
# the command line.
#
# Usage:
#
#   python hello.py [name]
#

import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = 'World'

print('Hello, %s!' % name)

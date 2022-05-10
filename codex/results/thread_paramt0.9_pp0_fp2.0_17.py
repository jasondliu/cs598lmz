import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
0
0
0
# good
"""
{'cell_type': 'markdown', 'metadata': {}, 'source': ["# good", '', 'import sys, threading', 'threading.Thread(target=lambda: sys.stdout.write("hello\\n")).start()', '0', '', '0', '', '0']}
"""
# good
%matplotlib inline
import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
0
0
0
--

python2
%matplotlib inline
import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
0
0
0

python3
%matplotlib inline
import sys, threading
threading.Thread(target=lambda: sys.stdout.write('hello\n')).start()
0
0
0

python2
%matplotlib inline
import sys, threading
thread

import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()

import time
time.sleep(3)
print('done')
</code>
The output:
<code>$ python test.py
done
</code>
But it works perfectly well in Python 2:
<code>$ python2 test.py
....done
</code>
I know that <code>sys.stdout.write</code> isn't thread-safe, but I think I'm not doing anything wrong here.


A:

That's because in Python 3, <code>sys.stdout</code> is a <code>TextIOWrapper</code> object (see the docs), which is not thread-safe. In Python 2, it's a <code>file</code> object which is thread-safe.
You can work around this by doing:
<code>import sys, threading
threading.Thread(target=lambda: sys.stdout.buffer.write('.')).start()

import time
time.sleep(3)
print('done')
</code>
The output:
<code>$ python3 test.py

import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b]2;NEW_THREAD\x07")).start()

# OR

import threading
threading.Thread(target=lambda: "\x1b]2;NEW_THREAD\x07").start()

# OR

import threading
threading.Thread(target=lambda: print("\x1b]2;NEW_THREAD\x07")).start()
</code>
But all of them still give me <code>UnicodeEncodeError: 'charmap' codec can't encode character '\x1b' in position 0</code> in the terminal.
I tried to change the encoding of <code>sys.stdout</code> to <code>UTF-8</code> but it didn't help.
On this question I found how to change the terminal title with a thread that calls <code>print</code> and I wonder why <code>print</code> works but not <code>sys.stdout.write</code>.
What am I missing?


import ctypes
ctypes.CDLL('/lib64/libc.so.6')
open('/dev/null', 'wb').close()
</code>
Run this script in a <code>screen</code> session with the <code>#{SHELL}</code> task mapped to <code>login</code>, and it works.  However, if you run this in <code>tmux</code>, then <code>tmux</code> crashes.  Bug report for this has been submitted.


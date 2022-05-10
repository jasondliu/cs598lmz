import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import subprocess
subprocess.call(["python", "-c", "import gtk; gtk.main()"])
</code>
The terminal will show <code>^C</code> but the program won't stop.
But the following code works well:
<code>import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gtk
gtk.main()
</code>
So, what's the problem?


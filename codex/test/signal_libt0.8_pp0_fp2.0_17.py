import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import subprocess
subprocess.call(["python", "-c", "import gtk; gtk.main()"])

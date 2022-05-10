import sys, threading
threading.Thread(target=lambda: sys.stderr.write("Hello\n")).start()
</code>
If you want to force display in the notebook, you can call <code>tk._default_root.update_idletasks()</code>, but I would not recommend that, since it is easy to accidentally freeze the notebook:
<code>import tkinter
import sys, threading

def threaded():
    sys.stderr.write("Hello\n")
    # ensure the output is displayed now
    tkinter._default_root.update_idletasks()

threading.Thread(target=threaded).start()
</code>


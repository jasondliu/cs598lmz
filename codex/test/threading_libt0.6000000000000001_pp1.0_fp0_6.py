import threading
threading.stack_size(2**27)

w = Tcl()

# The following code is added during CI.
# It works around a tkinter issue that causes application crashes
# on certain versions of MacOS when using Tcl/Tk 8.5.
if platform.system() == "Darwin" and platform.mac_ver()[0] >= "10.15":
    w.eval('package require -exact tk 8.6')

w.title("LED Controller")

# Change font size
w.tk.call('tk', 'scaling', 1.5)

w.mainloop()

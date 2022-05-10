import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_VIRTUAL, 0.5)
signal.pause()

# Since Python is not built as a multithreaded application, the Python
# interpreter only runs in one operating system thread at a time: your program
# is either running Python code, or it’s running code in some other language
# (for example, C code that came from an extension module).
# This means that if the Python interpreter is blocked on some C function or
# I/O operation, there is no way to handle a signal.

# This is a problem if you want to use signals as a way of interrupting a
# long-running Python computation. Normally, a Python thread is responsive to
# signals because it “occasionally” checks for signals while it is running
# bytecode. If your Python code is doing a long-running computation in C, you
# might need to use a separate thread that occasionally interrupts your main
# C computation to check for signals.

# There are some important details to keep in mind when you implement this
# sort of signal handling. First, your Python thread must

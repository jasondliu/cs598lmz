import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
</code>
One final note.  This approach will block your program from doing anything else until the user has dismissed the message box.  If you don't want your program to block, you can put it in a new thread.  The other poster to this thread suggested creating a new process.  While that is possible, that is an expensive operation and wasteful.  If you multi-thread your program, you can use QThread to do the multithreading for you.  If you use raw Python threads, you will need to use <code>QCoreApplication.processEvents()</code> to keep the GUI alive.


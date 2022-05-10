import sys, threading

def run():
    x = 1
    sys.stdout.write("1")
    threading.Timer(0.5, run).start()

run()
</code>
So, I want it to run on the background where I can do other stuff when the countdown is going on.
The script above works as it is supposed to, but I can't do anything else while the script is running.
Cheers,
Anonnoymous


A:

This isn't so much a Python-related question. Your problem is that the script won't terminate unless you do a <code>sys.exit()</code>, since the main thread is holding the script open. You can tell this via the process manager if you're on Linux or OS X, or the Task Manager on Windows--there's a python.exe process that's running as long as your script is running.
The easiest potential fix would be to change your definition of <code>run</code> to include a <code>sys.exit()</code> call. Another option would be to use multiprocessing to make a new process from the thread, or write your script so that the main thread itself is the clock

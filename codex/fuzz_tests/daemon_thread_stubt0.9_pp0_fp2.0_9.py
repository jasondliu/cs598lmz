import sys, threading

def run():
    while True:
        cmd = input('')
        if cmd == "stop" or cmd == "start":
            print('received:', cmd)
            sys.exit(0)

proc = Process(target=run)
proc.daemon = True
proc.start()

for i in range(3):
    print('pass')
    time.sleep(1)
</code>
Use as follows:
<code>C:\dev&gt;python3 t.py
pass
pass
pass
start
received: start

C:\dev&gt;
</code>


A:

The problem
The displayed process is a child process spawned by the first process. Both the parent and child appear in the process lists with the same name (it has not been changed via <code>setproctitle</code>), and both are running scripts with the same name. The script of interest is one level down the tree in the hierarchy. I.e the script is being launched by the Python process, itself launched by the first level Python process.
Here's the tree from <code>psutil</code>
<code>&

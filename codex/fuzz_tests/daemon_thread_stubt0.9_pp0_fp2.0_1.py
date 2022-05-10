import sys, threading

def run():
    print("Start process with PID {0}.".format(os.getpid()))
    input()
    print("Stop process with PID {0}.".format(os.getpid()))
    sys.exit(0)

if __name__ == "__main__":
    process = multiprocessing.Process(target=run)
    process.start()
    process.join()
    print("Joined with process {0} with exit code {1}.".format(process.pid, process.exitcode))
</code>
The code above works great; it spawns a child process and waits at <code>process.join()</code> until the child terminating.
However I cannot seem to map <code>os.getpid()</code> in the child process to its corresponding <code>Process</code> since <code>Process</code> has no getter for <code>Process.pid</code>, nor does it have any properties attached to it.
I would like to create a <code>dict()</code> of <code>Process.pid</code> to <code>Process</code> which will allow

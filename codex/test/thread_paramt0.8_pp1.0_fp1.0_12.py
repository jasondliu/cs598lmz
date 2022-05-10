import sys, threading
threading.Thread(target=lambda:sys.stdout.write("\n")).start()

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

# Now launch the command
process = subprocess.Popen(['bash', '-c', './out/bin/host/x86_64-linux-gnu/serial'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Launch the thread to read stdout of the child process
q = Queue()
t = threading.Thread(target=enqueue_output, args=(process.stdout, q))
t.daemon = True
t.start()

# Use `q.get()` to block/wait and get the output of the child process
process.stdout.close()
process.terminate()
t.join()

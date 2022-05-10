import select
# Test select.select()

def communicate(s, pipe_stdin, pipe_stdout):
    while True:
        # Wait until there is data to do something with
        readables, writeables, exceptions = select.select([pipe_stdin, s], [], [])
        if pipe_stdin in readables:
            data = os.read(pipe_stdin, 1024)
            if not data: # end of file
                break
            s.sendall(data)
        if s in readables:
            data = s.recv(1024)
            if not data: # EOF
                break
            os.write(pipe_stdout, data)

import subprocess

# Start the subprocess
p = subprocess.Popen(['ssh', 'some.remote.machine'],
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                     bufsize=0, # unbuffered
                     close_fds=True)

# Connect the pipes
communicate(p.stdout.fileno(), sys.stdin.fileno(), sys.std

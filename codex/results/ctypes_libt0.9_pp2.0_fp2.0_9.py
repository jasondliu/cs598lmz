import ctypes
ctypes.windll.user32.MessageBoxW(0, "Test", "python to user32", 0)

# similar to os.spawnlpe
def run_command(command, env=os.environ):
    pid = os.getpid()
    rc = os.fork()
    if rc < 0:
        print('fork failed, returning %d' % rc, file=sys.stderr)
        sys.exit(1)
    elif rc == 0:                   # child
        os.execlpe(command, command, str(pid), '0', env)
        assert False, 'error starting program'

run_command('python', env={'HOME': '/tmp'})

import subprocess
pro = subprocess.Popen('python')
pro.communicate('once upon a time...\n')
pro.wait()
"""
"""
import subprocess

print "reading..."
proc = subprocess.Popen(['python'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
stdout_value

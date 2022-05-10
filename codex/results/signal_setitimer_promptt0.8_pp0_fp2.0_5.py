import signal
# Test signal.setitimer()

class AlarmException(Exception):
    pass

def alarm_handler(signum, frame):
    raise AlarmException

def non_block_read(fd):
    fd.setblocking(0)
    total_data = []
    data = ''
    while True:
        try:
            data = fd.read()
            if data:
                total_data.append(data)
                return ''.join(total_data)
            else:
                return ''
        except:
            pass

def get_command_output(cmd):
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, 0.1)
    try:
        p = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = p.stdout, p.stderr
        # stdout = non_block_read(p.stdout)

import signal
# Test signal.setitimer to generate periodic timer
# signals

def handler(signum, frame):
    print('Alarm!')

def non_block_read(output):
    fd = output.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
    try:
        return output.read()
    except:
        return ""


if __name__ == "__main__":
    p = subprocess.Popen('echo_test', shell=True, stdout=subprocess.PIPE)
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 1, 0.5)
    while True:
        signal.pause();
        print(non_block_read(p.stdout))

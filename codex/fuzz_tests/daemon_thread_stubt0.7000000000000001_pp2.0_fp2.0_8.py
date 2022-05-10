import sys, threading

def run():
    p = subprocess.Popen(['python', '-u', '-m', 'vizdoom'] + sys.argv[1:], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    thr = threading.Thread(target=p.communicate)
    thr.daemon = True
    thr.start()

    while True:
        try:
            cmd = sys.stdin.readline().strip()
            if cmd.startswith('save_video'):
                p.stdin.write(cmd + '\n')
                p.stdin.flush()
                p.stdin.write(sys.stdin.read())
                p.stdin.flush()
            elif cmd == 'quit':
                p.stdin.write('quit\n')
                p.stdin.flush()
                break
        except KeyboardInterrupt:
            break

    p.wait()
    thr.join()
    sys.stdout.write(p.stdout.read())


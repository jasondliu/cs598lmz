import signal
signal.signal(signal.SIGINT, lambda sig, frame: print(""))

cmds = []
for path in sys.argv[1:]:
    cmds.append(('df', path))
cmds.append(('du', '-hs'))
cmds.append(('free', '-m'))
cmds.append(('mpstat', '-qP', 'ONLN'))

pipes = []
for cmd in cmds:
    with subprocess.Popen(cmd, stdout=subprocess.PIPE) as proc:
        pipes.append(proc)

while pipes:
    for pipe in pipes[:]:
        try:
            msg = pipe.stdout.readline().decode().strip()
            if not msg:
                pipes.remove(pipe)
            else:
                print(msg)
        except:
            pipes.remove(pipe)

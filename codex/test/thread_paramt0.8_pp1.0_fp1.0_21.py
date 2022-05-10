import sys, threading
threading.Thread(target=lambda:
                 sys.stdin.readline()).start()

if sys.argv[1] == 'run':
    sys.path.append('/Users/ashleychen/repos/rosetta/main/source')
    import pyrosetta
    pyrosetta.init()

    import os, sys, subprocess
    command = ' '.join(sys.argv[2:])
    status = os.WEXITSTATUS(os.system(command))
    subprocess.call(
            ['growlnotify', '-m', command])

    sys.exit(status)

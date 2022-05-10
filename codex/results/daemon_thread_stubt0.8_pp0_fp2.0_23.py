import sys, threading

def run():
    cmd = sys.argv
    for i in range(4):
        cmd.pop(0)
    if 'R' in cmd:
        cmd.remove('R')
    if 'r' in cmd:
        cmd.remove('r')
    if 'i' in cmd:
        cmd.remove('i')
    if 'I' in cmd:
        cmd.remove('I')
    if ('t' in cmd or 'T' in cmd) and ('n' in cmd or 'N' in cmd):
        cmd.remove('t')
        cmd.remove('n')
    if 't' in cmd or 'T' in cmd:
        cmd.remove('t')
        cmd = ' '.join(cmd)
        print (cmd)
        os.system(cmd)
    elif 'n' in cmd or 'N' in cmd:
        cmd.remove('n')
        cmd = ' '.join(cmd)
        print (cmd)
        os.system(cmd)
    else:
        cmd = ' '.join(cmd)
        print (cmd)
        os.

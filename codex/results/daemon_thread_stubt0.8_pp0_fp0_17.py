import sys, threading

def run():
    structs = []
    cache = {}
    while True:
        cmd = sys.stdin.readline()
        if cmd == 'cleanup\n':
            #print ''
            sys.stdout.flush()
            #return
        elif cmd[0:7] == 'struct ':
            for i in cmd[7:].split(','):
                if i.strip() not in structs:
                    structs.append(i.strip())
        elif '=' in cmd:
            if cmd.strip()[0] != '#':
                var, val = cmd.strip().split('=')
                val = val.strip()
                var = var.strip()
                if var not in structs:
                    print var, '=', val
                    sys.stdout.flush()
                    cache[var] = val
                else:
                    if var not in cache:
                        cache[var] = {}
                    if val[0] == '{':
                        array = {}
                        for i in val[1:-1].split(','):
                            if i.strip():

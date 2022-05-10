import sys, threading

def run():
    phase = 'stop'
    for c in itertools.cycle('|/-\\'):
        if phase == 'stop':
            sys.stdout.write('\r| stop')
            break
        elif phase == 'run' or phase == 'stream':
            sys.stdout.write('\r| record audio stream')
            phase = 'stream'
        else:
            sys.stdout.write('\r| processing {}'.format(c))
            time.sleep(0.1)

t = threading.Thread(target=run, daemon=True)
t.start()

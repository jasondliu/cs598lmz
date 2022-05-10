import sys, threading

def run():
    while True:
        a = raw_input('')
        if 'print' in a:
            es.server.cmd(a)

not_threading = False
if len(sys.argv) > 1:
    if sys.argv[1] == 'disable_threading':
        not_threading = True

if not not_threading:
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    es.server.cmd('alias es_console interrupt')
else:
    def es_console():
        a = raw_input('')
        if 'print' in a:
            es.server.cmd(a)
        es_console()
    es_console()

def load():
    es.precachesound('misc/talk.wav')
    es.log('Console has loaded.')

    if not not_threading:
        es.server.cmd('alias es_console interrupt')
    else:
        es_console = input_plus

def unload():
    es

import sys, threading

def run():
    while True:
        line = raw_input()
        if line == 'exit':
            sys.exit()
        else:
            print 'Input:', line

threading.Thread(target=run).start()

print 'Thread started'
</code>
Or use <code>threading.Thread</code> with a function that takes <code>args</code> and <code>kwargs</code> arguments:
<code>import sys, threading

def run(args, kwargs):
    while True:
        line = raw_input()
        if line == 'exit':
            sys.exit()
        else:
            print 'Input:', line

threading.Thread(target=run, args=(), kwargs={}).start()

print 'Thread started'
</code>


import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

# from https://stackoverflow.com/questions/542092/how-to-redirect-stdout-in-python
class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush() # If you want the output to be visible immediately
    def flush(self) :
        for f in self.files:
            f.flush()

sys.stdout = Tee(sys.stdout, open('/dev/pts/1', 'w'))

import time

#from IPython.lib import backgroundjobs as bg
#from IPython.core.magic import register_line_magic

#jobs = bg.BackgroundJobManager()

#@register_line_magic
#def job(line):
#    jobs.new(line)
#    print('job started')

#%job sleep 10
#%job sleep 10


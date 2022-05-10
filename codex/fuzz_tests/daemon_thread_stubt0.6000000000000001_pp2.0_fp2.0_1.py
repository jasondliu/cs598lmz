import sys, threading

def run():
    p = subprocess.Popen(['python', 'stderr-tee.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    print 'stdout:', stdout
    print 'stderr:', stderr

threading.Thread(target=run).start()
</code>
Output:
<code>stdout: 
stderr: Traceback (most recent call last):
  File "stderr-tee.py", line 4, in &lt;module&gt;
    sys.stderr = Tee(sys.stderr, open('/tmp/log', 'a'))
  File "stderr-tee.py", line 2, in __init__
    self.file = file
TypeError: coercing to Unicode: need string or buffer, file found
</code>


from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# In[9]:

import subprocess
subprocess.run(['ls', '-l'])

# In[10]:

try:
    retcode = subprocess.call("ls")
    if retcode < 0:
        print("Child was terminated by signal", -retcode, file=sys.stderr)
    else:
        print("Child returned", retcode, file=sys.stderr)
except OSError as e:
    print("Execution failed:", e, file=sys.stderr)

# In[11]:

subprocess.call("echo $PATH", shell=True)

# In[12]:

p = subprocess.Popen(['/

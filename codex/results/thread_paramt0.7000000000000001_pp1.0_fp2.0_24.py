import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()
</code>
You can also use <code>os.system</code>:
<code>import os
os.system('echo -e "\a"')
</code>


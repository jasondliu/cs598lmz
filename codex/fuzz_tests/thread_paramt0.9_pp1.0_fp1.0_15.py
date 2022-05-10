import sys, threading
threading.Thread(target=lambda: sys.stdout.write("I like \u2764 in Python\n")).start()\n',
       b'import sys, threading\nthreading.Thread(target=lambda: eval("sys.stdout.write(\'"\'"\\x1b[1;34m\\n\\x1b[0;34m|  \\x1b[1;34m\\x1b[1;32m@author\\x1b[0m \\x1b[1;32m=\\x1b[0m \\x1b[1;34m"Javier Osuna"\\x1b[0;34m\\n\\x1b[0;34m\\x1b[1;34m|  \\x1b[1;34m\\x1b[1;32m@project\\x1b[0m\\x1b[1;34m \\x1b[0m \\x1b[1;34m=\\x1b[0m \\x1b[1;34m"I like \u2764"\\x1b[0;34m\\

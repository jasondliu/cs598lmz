import sys, threading
threading.Thread(target=lambda: sys.stdout.write('hello\n')).start()

import os
os.system('echo "hello"')

import subprocess
subprocess.Popen('echo "hello"', shell=True)

import asyncio
asyncio.run(b'hello')

import multiprocessing
multiprocessing.Process(target=b'hello').start()

import curses
curses.wrapper(b'hello')

import platform
platform.system(b'hello')

import socket
socket.gethostbyname_ex(b'hello')

import subprocess
subprocess.Popen(b'hello', shell=True)

import os
os.system(b'hello')

import os
os.spawnl(os.P_NOWAIT, b'hello', b'hello')

import subprocess
subprocess.Popen(b'hello', shell=True)

import subprocess
subprocess.Popen(b'hello', shell=True)

import subprocess
subprocess.Popen(b'hello', shell=True)



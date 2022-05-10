import socket
socket.if_indextoname(3)

import os
os.geteuid()

os.getpid()
os.getppid()
os.getgid()
os.getpgid()
os.getgroups()
os.getuid()

import pwd
pwd.getpwuid(uid)
pwd.getpwnam('root')

import grp
grp.getgrgid(uid)

os.getenv('PATH')
os.setenv('java', '/usr/bin')
os.getenv('java')

os.listdir()
os.listdir('.')
os.listdir('./..')
os.getcwd()
os.chdir('/')
os.getcwd()
os.chdir('/home/vladimir')
os.getcwd()

import time
#time.sleep(5)

time.sleep(10)



import random
random.randint(15, 18)
random.randint(15, 18)
random.randint(15, 18)

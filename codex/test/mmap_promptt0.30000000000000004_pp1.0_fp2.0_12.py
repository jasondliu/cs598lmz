import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, 0, 0)

import os
# Test os.getcwd(), os.listdir(), os.mkdir(), os.rmdir(), os.unlink(), os.stat(), os.statvfs(), os.system(), os.environ

import pwd
# Test pwd.getpwuid(os.getuid()).pw_name

import random
# Test random.random(), random.randint(0, 1000000000), random.choice("abcdefghijklmnopqrstuvwxyz0123456789"), random.sample(xrange(100), 10)

import re
# Test re.compile("foo.*")

import select
# Test select.select([sys.stdin], [], [], 0)

import socket
# Test socket.socket(), s.connect(("www.python.org", 80)), s.send("GET / \n"), s.recv(1000), s.close()

import string
# Test string.letters, string.lowercase, string.upp

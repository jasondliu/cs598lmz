import socket
socket.if_indextoname(4)

import sys
print(sys.maxsize)

#sys.stdout.write("a\n")

import sys
type(sys.stdout)
print("hello, world")
print("hello", "world")
print("hello", "world", sep="--")
print("hello", end="***")
print("world")
print("hello", file=sys.stderr)

import sys
print("hello, world", file=sys.stdout)
print("hello", "world", file=sys.stdout)
print("hello", "world", sep="--", file=sys.stdout)
print("hello", end="***", file=sys.stdout)
print("world", file=sys.stdout)

import sys
print("hello, world", file=sys.stdout)
print("hello", "world", file=sys.stdout)
print("hello", "world", sep="--", file=sys.stdout)
print("hello", end="***", file=sys.stdout)
print("world", file=sys.stdout)


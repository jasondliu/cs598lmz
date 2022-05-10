import select
# Test select.select()

from socket import *
import time
import sys

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 0))
s.listen(1)

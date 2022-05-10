import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(map(str, sorted(map(int, sys.stdin.read().split())))))).start()

####################################################################################################################################################################################################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 14:02:12 2018

@author: gray
"""

from threading import Thread

def print_numbers(n):
    while True:
        print(n)
    return

for i in range(1, 10):
    thread = Thread(target=print_numbers, args=[i])
    thread.start()

####################################################################################################################################################################################################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 14:05:17 2018

@author: gray
"""

import os
from threading import Thread

def print_numbers(n):
    while True:
        print(n)
    return

for i

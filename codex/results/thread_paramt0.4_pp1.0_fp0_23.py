import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32m' + input() + '\x1b[0m' + '\n')).start()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, threading

def get_input(color):
    def input_thread(L):
        L.append(sys.stdin.readline())
    L = []
    sys.stdout.write("\x1b[1;%dm" % (30+color))
    threading.Thread(target=input_thread, args=(L,)).start()
    return L

L = get_input(37)
while True:
    if L:
        print(L[0], end="")
        L = get_input(37)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, threading

def get_input(color):
    def input_thread(L):
        L.append(sys.std

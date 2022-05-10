import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join(sorted(sys.stdin.read().split('\n'))))).start()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読

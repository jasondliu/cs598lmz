import select
# Test select.select()
from time import time
import os
import sys

PIPE_PREFIX = "/run/user/" + str(os.getuid()) + "/mpv"

"""
Traducir una string con argumentos a una lista de strings a pasar a popen
con args modo shell=False
"""
def str_to_tokens(s='', ws=' '):
    l = len(s)
    if l == 0: 
        return []
    tokens = []
    curr = 0
    level = 0
    quote = False
    non_ws = False
    while curr < l:
        if s[curr] == '\'' or s[curr] == '"' or s[curr] == '`':
            quote = s[curr]
        elif s[curr] == '(' or s[curr] == '[':
            level += 1
            non_ws = False

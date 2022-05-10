import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()

def is_unique(string):
    d = {}
    for ch in string:
        if ch in d:
            return False
        d[ch] = 1
    return True

def sort_string(string):
    string = list(string)
    string.sort()
    return ''.join(string)

def is_permutation(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    string_1 = sort_string(string_1)
    string_2 = sort_string(string_2)
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            return False
    return True


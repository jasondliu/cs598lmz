import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)


class Node(object):
    def __init__(self, typ, val, children):
        self.typ = typ
        self.val = val
        self.children = children


class Environment(object):
    def __init__(self, parent=None, vars=None):
        self.parent = parent
        self.vars = vars or {}

    def lookup(self, id):
        if id in self.vars:
            return self.vars[id]
        return self.parent.lookup(id)

    def new_var(self, id):
        self.vars[id] = None

    def set_var(self, id, val):
        self.vars[id] = val


def main():
    env = Environment()
    env.new_var('print')
    env.set_var('print', print)
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        if not s:
            continue
        try:


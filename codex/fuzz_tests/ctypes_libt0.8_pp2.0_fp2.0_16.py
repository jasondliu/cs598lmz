import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
# user32.dll
```

```python
# Python 3
# Windows
from tkinter import messagebox
messagebox.showinfo("Title", "Your text")
```

```python
# Python 2
# Windows
from Tkinter import Tk
root = Tk()
root.withdraw()
messagebox.showinfo("Title", "Your text")
```

<a name="error-handling"></a>
### Error Handling

```python
try:
    f = open('testfile','w')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()
```

```python
try:
    f = open('testfile','r')
    f.write('Test write this')
except IOError:
    #

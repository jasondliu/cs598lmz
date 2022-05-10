import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# This will produce a warning message:
import ctypes
ctypes.windll.user32.MessageBoxW("Your text", "Your title", 1)
```

```python
def print_message(msg):
    print(msg)

print_message("Hello World") # This is fine

# This is not fine and will produce a warning message:
print_message(msg="Hello World")
```

```python
# This is fine
for i in range(1, 5):
    print(i)

# This is not fine and will produce a warning message:
for i in range(1, 5):
    print i
```

```python
# This is fine
if True:
    print("Hello World")

# This is not fine and will produce a warning message:
if True: print("Hello World")
```

```python
# This is fine
[i for i in range(1, 5)]

# This is not fine and

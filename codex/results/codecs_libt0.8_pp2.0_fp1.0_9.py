import codecs
codecs.open("file", "r", "utf_8")
```
2. 
```
import sys
import codecs
sys.stdout = codecs.getwriter("utf_8")(sys.stdout)
```

## Use `string.maketrans()` to remove punctuation

```
import string

# Sample string
my_str = "Hello!!!, he said ---and went."

# Make translation table
table = my_str.maketrans("", "", string.punctuation)

# Remove punctuation
out = my_str.translate(table)

# Print string
print(out)
```

## Use `pyperclip` to copy and paste

```
pip install pyperclip
```

```
import pyperclip

pyperclip.copy("Hello World")
pyperclip.paste()
```

## File type

File extension indicates the file type and what application can open it.

To get file name and extension:
```
import os

split = os.

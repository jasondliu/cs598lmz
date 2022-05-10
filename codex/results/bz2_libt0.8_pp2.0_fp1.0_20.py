import bz2
bz2.compress()
```

```python
import bz2
bz2.decompress()
```

```python
import zlib
zlib.compress()
```

```python
import zlib
zlib.decompress()
```

```python
import gzip
gzip.open()
```

## File formats and compression
### Reading and unzipping files
Your boss has e-mailed you a zip file containing the text files of some articles he is reading for his research. In this exercise, you'll unzip the file and read the files into a dictionary.

The zip file is available as a file called articles.zip.

**Instructions**

- Import the zipfile module.
- Create a ZipFile object by passing it the string 'articles.zip' and then use its extractall() method to extract all the contents of the archive in the current directory.
- Import the re module, using the abbreviated form re.
- Use the re.findall() function to extract all words from file_name and append the words to the list words.


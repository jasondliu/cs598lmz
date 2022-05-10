from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b[:8])

```


```python
import tarfile
```


```python
with tarfile.open("enron.tgz") as tar:
    tar.extractall('./enron')
```


```python
enron_dir = './enron/enron_mail_20110402/maildir'

names = ["".join(["enron_mail_20110402/maildir/", name, "/", folder])
                 for name in os.listdir(enron_dir) 
                 if os.path.isdir("".join([enron_dir, name])) 
                 for folder in os.listdir("".join([enron_dir, name]))]

names = [name
         for name in names if name[-8:] == "sent_items"]

emails = [mail for folder in names for mail in os.listdir(folder)]

emails = [mail for mail in emails if mail[-4:] == ".txt"]

len(emails)
``

from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

```

```
import requests
requests.get(url).content

```

```
def download_all_files(source_file):
    with open(source_file, 'r') as fp:
        data = fp.read()
        fp.close()
    url = "https://files.rcsb.org/download/{}.pdb.gz"
    flist = data.split('\n')
    for line in flist:
        content = download_url_to_string(url.format(line))
        if line:
            with open('pdb/' + line + '.pdb', 'wb') as fp:
                fp.write(content)
                fp.close()
```

```

```

```

```

```

```

```

```

import lzma
lzma.compress()
```

[bzip2 (python 2)](https://docs.python.org/2/library/bz2.html)
```
import bz2
```


## Parsing and extracting data

### XML

```xml
<items>
    <item id="1">
        <title>Title text1</title>
        <body>Some body text</body>
    </item>
    <item id="2">
        <title>Title text2</title>
        <body>Some body text</body>
        <author>Alan Turing</author>
    </item>
    <item id="3">
        <title>Title text3</title>
        <body>Some body text</body>
        <author>The Rockefellers</author>
    </item>
</items>
```

Use **[xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html)**
```
import xml.etree.ElementTree as ET


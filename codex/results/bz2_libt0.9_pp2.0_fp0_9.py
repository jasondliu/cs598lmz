import bz2
bz2.open("test.xml.bz2")
```

```python
>>> bz2.open("test.xml.bz2")
<bz2.BZ2File name='test.xml.bz2' mode='r' compresslevel=9>

```

```python
>>> bz2.open("test.xml.bz2").read()
b'<?xml version="1.0" encoding="UTF-8"?>\n<root>\n  <row Id="1" PostTypeId="1" AcceptedAnswerId="2" CreationDate="2015-05-13T23:58:30.457" Score="6">\n    <Tags>&gt;docker&lt;/Tags>\n    <Title>Docker (http) to Docker ...</Title>\n  </row>\n  <row Id="2" PostTypeId="2" ...'

```

### XML

```python
>>> import xml.etree.ElementTree as ET 
>>> tree = ET.parse("test.xml.bz2")

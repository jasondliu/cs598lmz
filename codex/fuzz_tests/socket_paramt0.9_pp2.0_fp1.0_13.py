import socket
socket.if_indextoname(371)
```

#### Base64 Encoding & Decoding

```python
import base64
base64.encodebytes(b'123')
base64.decodebytes(b'MTIz')
```

#### Convert hex to base64

```python
import codecs
base64.b64encode(codecs.decode('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d', 'hex')).decode()
```

#### Convert base64 to hex

```python
codecs.encode(base64.b64decode('NDkyNzZkMjA2YjY5NmM2YzY5Nm5nNzk2Zzc1NzIyYjI2OTE2OTI5NWwxYzY5NmI2NTIxMjB2MDY5NmE1NzM2MTZ

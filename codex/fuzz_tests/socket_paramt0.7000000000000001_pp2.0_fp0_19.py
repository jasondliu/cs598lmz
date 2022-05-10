import socket
socket.if_indextoname(3)
# 'en0'
```

### Accessing the MacOSX System Configuration Library

```python
from mac_sys_cfg import SystemConfiguration

sc = SystemConfiguration()

sc.get(None, 'HostName')
# 'macbook'

sc.set(None, 'HostName', 'my-new-name')

sc.get(None, 'HostName')
# 'my-new-name'

sc.write()

sc.get(None, 'HostName')
# 'macbook'

sc.write(True)

sc.get(None, 'HostName')
# 'my-new-name'
```

### Handling SIP

```python
from mac_sip import SIP

SIP().status()
# 'disabled'

SIP().enable()

SIP().status()
# 'enabled'

SIP().disable()

SIP().status()
# 'disabled'
```

### Querying the System Integrity Protection status

```python
from mac_sip import

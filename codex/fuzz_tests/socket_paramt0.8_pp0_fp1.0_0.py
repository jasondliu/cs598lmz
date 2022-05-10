import socket
socket.if_indextoname(3)

# get all interfaces at once
map(socket.if_indextoname, range(0,10))
```

```
ifconfig en0 | grep inet
```


```
# use struct library to map the raw byte data to Python tuples
import socket
import struct
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

import subprocess
ip = subprocess.check_output(["ifconfig en0 | grep inet | awk '{print $2}'"], shell=True)
print ip
```



# IPython/Jupyter

```
jupyter notebook --generate-config
# add password
passwd=''
ipython
In [

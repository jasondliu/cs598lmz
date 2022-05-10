import io
class File(io.RawIOBase):
    """An empty file."""
    def read(self, n=-1):
        """This is only be used as a parameter of tqdm iterator."""
        return b''
    
test_file = File()
t=TqdmUpTo(1000, file=test_file)
for x in t:
    pass
```

### Other Features
#### Manual Control
```python
from tqdm import trange
from time import sleep

for i in trange(15, desc="1st loop"):
    for j in trange(15, desc="2nd loop", leave=False):
        for k in trange(100, desc="3nd loop"):
            sleep(0.01)
```

#### Dynamic Messages / Plotting
```python
from tqdm import trange
from random import random, randint
from time import sleep

bar = trange(10)
for i in bar:
    bar.set_description("Loss: {:.3f}".format(random()))
    bar.refresh()
    sleep(0.1)

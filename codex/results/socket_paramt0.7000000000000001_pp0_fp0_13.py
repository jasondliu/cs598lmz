import socket
socket.if_indextoname(3)

import ipaddress
ipaddress.ip_address('127.0.0.1')

import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(os.environ)

# %%

d = {'apple':1, 'orange':2}
d['apple']
d['banana'] = 3
d

# %%

d2 = {'apple':1, 'orange':2, 'banana':5}
d.update(d2)
d

# %%

d.pop('orange')

# %%

d.popitem()

# %%

d.clear()

# %%

d = {'apple':1, 'orange':2, 'banana':5, 'apple':3}
d

# %%

d.setdefault('apple')
d.setdefault('peach', 4)
d

# %%

d.keys()

# %%

d.values()

# %%

d.items()

# %%

for i in d

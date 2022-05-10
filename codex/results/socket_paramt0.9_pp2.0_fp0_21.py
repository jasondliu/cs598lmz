import socket
socket.if_indextoname(7)

socket.inet_aton(b'192.168.100.100')
socket.inet_ntoa(b'\xc0\xa8\x64\x64')

import hashlib
import hmac

digest_maker = hmac.new('secret_shared_key', b'some data', hashlib.sha1)
digest_maker.hexdigest()
digest_maker.update(b'some more data')
digest_maker.hexdigest()

from collections import OrderedDict

INCOMING = OrderedDict(
    first_name=None,
    last_name=None,
)

post = {
    'first_name': 'Jason',
    'last_name': 'Mraz',
}

clean_data = {
    k: v
    for k, v in post.iteritems()
    if k in INCOMING
}

clean_data

from collections import namedtuple

from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

my_car

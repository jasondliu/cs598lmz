import threading
threading.stack_size(2**29)

from six import itervalues
from six.moves import urllib
import sys

from bs4 import BeautifulSoup
import redis


def main():
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

    r = redis.StrictRedis(connection_pool=pool)

    if r.get('fetched'):
        print('already fetched')
        sys.exit(0)

    with open('list.txt') as _f:
        result = _f.readlines()

    def set(x):
        r.set(x[0], x[1:])

    threads = []
    for result_item in result:
        k, v = result_item.split(':')
        v = v.strip().split(',')
        if len(v[0]) < 2:
            continue
        if k.startswith('www'):
            k = k.split('.')[1]

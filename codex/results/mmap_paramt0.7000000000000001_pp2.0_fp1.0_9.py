import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])

import os

# os.remove('test')

import pytest


@pytest.mark.parametrize('v', [1, 2, 3])
def test_func(v):
    pass

import os
import sys

print(sys.executable, os.path.dirname(sys.executable))

import datetime as dt

print(dt.datetime.now().strftime('%Y%m%d %H:%M:%S'))

from multiprocessing import Pool, Process


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

    p = Process(target=f, args=(2,))
    p.start()
    p.join()


from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)


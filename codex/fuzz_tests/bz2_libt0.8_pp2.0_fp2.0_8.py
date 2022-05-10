import bz2
bz2.decompress(bz2.compress(text))

import csv
import cStringIO
from datetime import date
import doctest
f = cStringIO.StringIO()
writer = csv.writer(f)
writer.writer.ow(('title 1', 'title 2', 'title 3'))
for i in range(3):
    writer.writerow(('value 1', 'value 2', 'value 3'))
 print f.getvalue()

from decimal import *
sum([Decimal('0.1')] * 10) == Decimal('1.0')

from fractions import Fraction
Fraction(1, 3)

from functools import partial
def power(base, exponent):
	return base ** exponent
power(2,4)
	
two_to_the = partial(power, 2)
two_to_the(3)

from hashlib import md5
md5(open('/etc/passwd').read()).hexdigest()

import heapq
a = []
heapq.heappush(a, 5)


import bz2
bz2.decompress(bz_data)

# In[ ]:

# decimal.Decimal.from_float returns the exact decimal equivalent of
# a floating point number
from decimal import Decimal
Decimal.from_float(0.1)


# In[ ]:

str(Decimal.from_float(0.1))


# In[ ]:

#The decimal module provides arithmetic with as much precision as needed.
1.1 + 2.2


# In[ ]:

Decimal(1) / Decimal('3')


# In[ ]:

format(0.1, '.15f')


# In[ ]:

format(Decimal.from_float(0.1), '.17')


# In[ ]:

# The fractions module provides support for rational number arithmetic.
from fractions import Fraction
x = Fraction(1, 3)
y = Fraction(4, 6)
print(x)
print(y)


# In[ ]:

print(Fraction('.25'))


# In[ ]:

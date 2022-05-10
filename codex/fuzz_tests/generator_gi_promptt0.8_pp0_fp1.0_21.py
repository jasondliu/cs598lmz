gi = (i for i in ())
# Test gi.gi_code, which should be a code object
#The second form creates a generator-iterator which is initialized to the same
# state as gen would be upon exit from a yield expression.

#In both forms, the module's __name__ attribute is used to determine the
# module name.

#Typical forms of generator expressions are:

#    sum(i*i for i in range(10))
#    sum(i*i for i in xrange(10))
#    sum(i*i for i in ifilter(None, range(10)))
#    sum(m.group(1) for m in re.finditer(r"(\d+)", "20121223"))

#However, the last two forms are not equivalent to the first two forms,
# unless you also import from __future__ the statement-based form of
# generator expressions from Python 2.4 or 2.5. The first two forms
# would translate into a for loop that builds a list of values, with the
# list kept entirely in memory. The last two forms use iterators that
# produce values on demand, not building a value list.



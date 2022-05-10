gi = (i for i in ())
# Test gi.gi_code.co_name.
name = gi.gi_code.co_name

assert name == ''

# A class that returns a generator iterator.
class GIC(object):
    def gi(self):
        return (i for i in (1,2,3))

gi = GIC().gi()
# Test gi.gi_code.co_name.
name = gi.gi_code.co_name

assert name == 'gi'

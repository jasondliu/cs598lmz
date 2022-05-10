gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_yieldfrom
class A:
    def __init__(self):
        self.val = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.val += 1
        if self.val > 10:
            raise StopIteration
        return self.val

a = A()
gi = (i for i in a)
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_yieldfrom

# Test gi.send(None)
gi.send(None)

# Test gi.send(1)
gi.send(1)

# Test gi.send(2)
gi.send(2)

# Test gi.send(3)
gi.send(3)

# Test gi.send(4)
gi.send(4)

# Test gi.send(5)


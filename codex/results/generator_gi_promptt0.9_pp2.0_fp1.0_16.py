gi = (i for i in ())
# Test gi.gi_code
print gi.gi_code.co_name
# Test gi.gi_frame
print gi.gi_frame.f_code.co_name

c = 3
class TestGI:
  def __init__(self):
    self.gi = (self.method() for i in xrange(c))

  def method(self):
    return 1

print TestGI().gi.gi_code
print TestGI().gi.gi_frame.f_code

def test_gi(gi):
  try:
    print gi.gi_code.co_name
    print gi.gi_frame.f_code.co_name
  except:
    print 'Unexpected error:', sys.exc_info()[0]

test_gi(gi)
TestGI.method(TestGI())
test_gi(TestGI().gi)

for e in gi:
  print e
"""

main()

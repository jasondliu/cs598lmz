gi = (i for i in ())
# Test gi.gi_code.co_flags; co_flags is available in Python 2.6 and upwards
print(gi.gi_code.co_flags)
t = Test()
print('created %s' % t)

# test getting the current frame
cf = sys._getframe()
print('sys._getframe(): %s' % cf)

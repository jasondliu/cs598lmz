gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("AttributeError")
# Test iter(gi) is gi
try:
    iter(gi) is gi
except TypeError:
    print("TypeError")
## Test next(gi)
#print(next(gi))
# Test gi.send(None)
try:
    gi.send(None)
except StopIteration:
    print("StopIteration")
# Test gi.close()
gi.close()
try:
    gi.send(None)
except StopIteration:
    print("StopIteration")
try:
    gi.close()
except StopIteration:
    print("StopIteration")
# Test gi.gi_running
try:
    print(gi.gi_running)
except StopIteration:
    print("TypeError")
try:
    print(gi.gi_running)
except AttributeError: ##
    print("AttributeError") # On Python 3.3, `gi` is cleared on `gi.close()`,
except

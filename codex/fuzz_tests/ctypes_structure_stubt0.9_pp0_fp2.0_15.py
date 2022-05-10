import ctypes

class S(ctypes.Structure):
    x = 1

# Note that s would not have a pointer to its class by default, you
# have to set it manually
s = S()
s._class_ = S
print(s._class_)
</code>
And here is the doc on the instance dictionaries.


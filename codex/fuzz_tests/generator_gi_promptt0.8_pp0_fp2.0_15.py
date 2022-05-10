gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame after assignment to gi.gi_frame
import sys

for i in gen_int.gi:
    if i == 5:
        gen_int.gi.gi_frame = sys._getframe()
    if i == 10:
        break
else:
    raise RuntimeError("Failed to execute loop")

for i in gen_int.gi:
    if i == 10:
        break
else:
    raise RuntimeError("Failed to execute loop")

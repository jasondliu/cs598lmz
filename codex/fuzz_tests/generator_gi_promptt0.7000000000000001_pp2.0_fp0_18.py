gi = (i for i in ())
# Test gi.gi_code==None.  Gi_code is None for simple generators.
gi.gi_code = None
gi.gi_code = 0

# Test gi.gi_frame==None.  Gi_frame is None for simple generators.
gi.gi_frame = None
gi.gi_frame = 0

# Test gi.gi_running==0.  Gi_running is 0 for simple generators.
gi.gi_running = 0
gi.gi_running = 0

# Test gi.gi_yieldfrom==None.  Gi_yieldfrom is None for simple generators.
gi.gi_yieldfrom = None
gi.gi_yieldfrom = 0

# Test gi.gi_yieldfrom.  Gi_yieldfrom is None for simple generators.
import re
gi.gi_yieldfrom = re.match
gi.gi_yieldfrom = 0

# Test gi_frame.f_lasti.
gi.gi_frame.f_lasti = 0
gi.gi_frame.f_lasti = 0

# Test gi_frame.f_

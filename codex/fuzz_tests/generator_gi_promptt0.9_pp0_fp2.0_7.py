gi = (i for i in ())
# Test gi.gi_code, gi.gi_frame, gi.gi_running, and gi.gi_yieldfrom
# with gi returning a generator that does not yield

gi = (i for i in ())
frame = gi.gi_frame
gi2 = gi.gi_yieldfrom
frame2 = gi2.gi_frame
gi3 = gi2.gi_yieldfrom
frame3 = gi3.gi_frame
gi4 = gi3.gi_yieldfrom
frame4 = gi4.gi_frame
gi5 = gi4.gi_yieldfrom
frame5 = gi5.gi_frame

# Test gi_running, gi_frame, and gi_code with direct calls to send()
# (does not use an intermediate frame)

gi2 = iter(())
gi2.send(1)
frame2 = gi2.gi_frame
gi3 = gi2.gi_yieldfrom
frame3 = gi3.gi_frame
gi4 = gi3.gi_yieldfrom
frame4 = gi

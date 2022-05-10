gi = (i for i in ())
# Test gi.gi_code is code object
tester.startGroup("gi.gi_code is code object")
try:
    tester.test("is code", gi.gi_code.__class__ == types.CodeType,
                "didn't return a code object")
    tester.test("code.co_argcount", gi.gi_code.co_argcount == 0,
                "didn't return an iterator with 0 args")
except:
    tester.error("raised an exception when called")
tester.groupDone()

# Test gi.gi_frame is frame object
tester.startGroup("gi.gi_frame is frame object")
try:
    tester.test("is frame", gi.gi_frame.__class__ == types.FrameType,
                "didn't return a frame object")
except:
    tester.error("raised an exception when called")
tester.groupDone()

# Test gi.gi_running is 1
tester.test("gi.gi_running is 1", gi.gi_running == 1,
            "didn't return an iterator

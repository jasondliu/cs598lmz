gi = (i for i in ())
# Test gi.gi_code (code object)
self.assertEqual(gi.gi_code.co_name, "")           # Changed in Python 2.6: AssertionError: "" != "<genexpr>"
self.assertEqual(gi.gi_code.co_firstlineno, 1)

# Test gi.gi_frame (frame object)
# f_back, f_code and f_trace are tested later
self.assertEqual(gi.gi_frame.f_lasti, 0)
self.assertEqual(gi.gi_frame.f_lineno, 1)
self.assertEqual(gi.gi_frame.f_restricted, 1)

self.assertIsInstance(gi.gi_frame.f_locals, dict)
self.assertEqual(gi.gi_frame.f_locals, {"i": i})

# Test gi.gi_running
self.assertEqual(gi.gi_running, 1) # Python 3: not defined

# Test gi.gi_yieldfrom
self.assertIsNone(gi.gi_yieldfrom)

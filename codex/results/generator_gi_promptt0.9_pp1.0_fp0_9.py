gi = (i for i in ())
# Test gi.gi_code
x = gi.gi_code
gi = (i for i in ('a', 'b'))
# Test gi.gi_frame
x = gi.gi_frame
class Crash:
    code = compile("yield 1", "scripts/sen/exprtest.script", "exec")
    def __iter__(self):
        return self
    def send(self, *args):
        exec(self.code)
        return None
gi = Crash.send(None)
# Test gi.gi_frame
x = gi.gi_frame
# Test gi.gi_running (should be 0)
gi = Crash.send(None)
x = gi.gi_running
# Test gi_running (should be 1)
gi = (i for i in 'abc')
x = gi.gi_running
# Test gi_running (should be 1)
gi = (i for i in 'abc').__next__()
x = gi.gi_running
# Test gi_running (should be 0)
gi = (i for i in 'abc')


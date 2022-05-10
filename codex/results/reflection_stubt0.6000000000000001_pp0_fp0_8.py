fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_code = b"\x01\x00\x00\x00"
fn.__code__.co_consts = (None, 0)
fn.__code__.co_lnotab = b"\x00"
fn()
'''

class Test:
    def __init__(self, n):
        self.n = n

    def __getitem__(self, key):
        return self.n + key

    def __call__(self, *args, **kwargs):
        return self.n

class Some:
    def __getitem__(self, key):
        return key

def run_tests(tests):
    for test in tests:
        test()

def test_opcode(opcode, args, expected, expected_stack):
    global interp
    interp.stack = []
    interp.push(args)
    interp.execute_opcode(opcode)
    assert interp.stack == [expected] + expected_stack, "opcode %s

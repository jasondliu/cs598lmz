fn = lambda: None
# Test fn.__code__

# These are set by dis.get_instructions below.
# We clear them during the test.
call_calls = None
jrel_calls = None
size_calls = None

def test_dis():
    global call_calls, jrel_calls, size_calls
    call_calls = jrel_calls = size_calls = 0
    def call_ex(instr):
        global call_calls
        call_calls += 1
        return True

    def jrel_ex(instr, instr_lb):
        global jrel_calls
        jrel_calls += 1
        return True

    def size_ex(instr):
        global size_calls
        size_calls += 1
        return True

    code = fn.__code__
    for i in dis.get_instructions(code):
        for group in dis.opmap, dis.opname, dis.hasjrel, dis.hasjabs, dis.hasjrel, dis.hasjabs, dis.hasarg, dis.

fn = lambda: None
# Test fn.__code__.co_code[0] == 64 and fn.__code__.co_code[1] == 185
# Test fn.__code__.co_code[2] == 235 and fn.__code__.co_code[3] == 74

# Starting v2.5, a HALTING_OPCODE (0x64) is added in front of the frame to mark
# it as a "fake frame".  This is not the opcode. Currently this is the next opcode:
# opcode_25plus = lambda: None
# Test opcode_25plus.__code__.co_code[0] == 64 and opcode_25plus.__code__.co_code[1] == 185
# Test opcode_25plus.__code__.co_code[2] == 235 and opcode_25plus.__code__.co_code[3] == 74

# A dummy error object that can used for frames that don't correspond to an error message.
DUMMY_ERROR = object()

class WaitForThreads(threading.Thread):
    """Run a function in a background

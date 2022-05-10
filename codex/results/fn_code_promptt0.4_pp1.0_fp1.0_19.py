fn = lambda: None
# Test fn.__code__
fn.__code__
# Test fn.__code__.co_code
fn.__code__.co_code
# Test fn.__code__.co_code[0]
fn.__code__.co_code[0]
# Test fn.__code__.co_code[0] == opcode.opmap['LOAD_CONST']
fn.__code__.co_code[0] == opcode.opmap['LOAD_CONST']
# Test fn.__code__.co_code[2]
fn.__code__.co_code[2]
# Test fn.__code__.co_code[2] == opcode.opmap['RETURN_VALUE']
fn.__code__.co_code[2] == opcode.opmap['RETURN_VALUE']
# Test fn.__code__.co_code[1]
fn.__code__.co_code[1]
# Test fn.__code__.co_code[1] == opcode.opmap['STORE_FAST']
fn.__code__.co_code[

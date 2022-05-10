import _struct
import re

def get_anonymous_opcodes(path):
    f = open(path)
    text = f.read()
    f.close()
    res = []
    for opcode in _dis.opname:
        res.append((opcode, len(re.subn('\W{}\W'.format(opcode), '', ' ' + text + ' ')[0])))
    return res
    
def get_anonymous_opcodes_from_bytecode(bytecode):
    res = []
    for opcode in _dis.opname:
        res.append((opcode, len(re.subn('\W{}\W'.format(opcode), '', ' ' + bytecode + ' ')[0])))
    return res

def get_utils(path):
    code = _compile(path)
    constants = []
    for const in code.co_consts:
        if type(const) == type(int):
            constants.append('{}'.format(const))

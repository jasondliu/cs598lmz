from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x5d\x00\x00\x80\x0e\xff')

# we have to implement opcodes ourselves!
# this means a lot of implementation of code

# opcode implementation

# REF: https://docs.python.org/3.6/library/dis.html
class Disassembler:
    # opcodes are python bytecodes
    # python bytecode is a list of opcodes

    def __init__(self):
        self.code = None
        self.code_index = 0
        self.opname = None
        self.oparg = None
        # offset into co_code of the last opcode argument
        self.extended_arg = 0
        self.prev_op = 0
        self.stacksize = 0
        self.labels = None
        
        # linestarts contains line numbers of the first instruction in each line
        self.linestart = None
        print('Disassembler Created!')
    
    def process_opargs(self):
        return None
    
    def dis(self

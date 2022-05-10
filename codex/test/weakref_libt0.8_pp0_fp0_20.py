import weakref

from typing import *

from . import instruction as _instruction


class InstructionSet(object):
    def __init__(self):
        from . import opcodes as _opcodes
        self.opcodes = {opcode.mnemonic: opcode for opcode in _opcodes.all_opcodes}
        self.functions = {}

    @property
    def int_register_width(self):
        return 16

    @property
    def int_register_count(self):
        return 8

    @property
    def pointer_register_count(self):
        return 8

    def register_function(self, mnemonic, function):
        self.functions[mnemonic] = function

    def get_function(self, mnemonic):
        return self.functions.get(mnemonic)

    def get_opcode(self, mnemonic):
        return self.opcodes.get(mnemonic)

    def get_instruction(self, mnemonic):
        opcode = self.get_opcode(mnemonic)
        return opcode.instruction

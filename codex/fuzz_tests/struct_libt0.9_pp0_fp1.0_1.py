import _structures.Runtime as r
import _structures.IntermediateCode as ic
import _structures.Operands as operands
import _structures.Operators as operators

###############################################################################################
# This module analyzes the code and outputs intermediate code, the symbol table and the runtime
# structures.

class Analyzer(object):
    def __init__(self, code):
        self.Op = operators.Operators()
        self.Operand = operands.Operands()
        self.code = code
        self.errors = list()
        self.tokens = list()
        self.operators = list()
        self.variables = dict()
        self.labels = dict()
        self.symbol_table = dict()
        self.ic = ic.IntermediateCode()
        self.runtime = r.Runtime()
        self.token = None
        self.line_number = 0

    def get_symbol(self, label, line_number):
        try:
            return self.symbol_table[self.labels.index(label)]
        except Exception

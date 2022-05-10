import gc, weakref
import re
import os
import sys

import ply.yacc as yacc
import ply.lex as lex

# local imports
import ast
import lexer
import parser
import ir

# for debugging purposes
import pprint

class CompilerError(Exception):
    pass

class Compiler(object):
    def __init__(self, source, filename='<input>', optimize=2, verbose=None):
        self.source = source
        self.filename = filename
        self.optimize = optimize
        self.verbose = verbose

    def get_ast(self):
        return ast.parse(self.source, self.filename)

    def compile(self):
        # generate the AST
        a = self.get_ast()

        # visit the AST
        v = ir.IRVisitor()
        v.visit(a)

        # optimize the IR
        if self.optimize > 0:
            v.optimize(self.optimize)

        # generate the IR
        return v.generate()

def main(argv):
   

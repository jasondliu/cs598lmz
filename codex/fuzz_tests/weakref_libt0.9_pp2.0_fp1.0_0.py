import weakref

import expression as ue_expression
import module as ue_module
import types as ue_types
import error as ue_error

import parser.constants as consts
import parser.lexer as lexer
import parser.ue_expressions as ue_expressions
import parser.ue_functions as ue_functions
import parser.ue_types as ue_prefix_types

class PascalParser(object):
    def __init__(self):
        self.__lexer = lexer.PascalLexer()
        self.__expr = ue_expressions.PascalUEExpressions()
        self.__functions = ue_functions.PascalUEFunctions()
        self.__types = ue_prefix_types.PascalUETypes()
        self.__parsed_modules = []

    def set_source(self, source):
        self.__lexer.set_source(source)

    def parse_module(self):
        module = ue_module.UEBaseModule()
        self.__parsed_modules

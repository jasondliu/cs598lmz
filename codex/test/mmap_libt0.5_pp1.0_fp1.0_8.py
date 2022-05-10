import mmap
import re

class SemanticError(Exception):
    def __init__(self, error_message, line_number):
        self.error_message = error_message
        self.line_number = line_number

class SyntaxError(Exception):
    def __init__(self, error_message, line_number):
        self.error_message = error_message
        self.line_number = line_number

class LexicalError(Exception):
    def __init__(self, error_message, line_number):
        self.error_message = error_message
        self.line_number = line_number

class Parser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.line_number = 1
        self.token_index = 0
        self.current_token = None
        self.current_token_type = None
        self.token_list = []
        self.symbol_table = {}
        self.jump_table = {}
        self.current_scope = 0
        self

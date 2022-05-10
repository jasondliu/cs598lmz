import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Info:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

class Function:
    def __init__(self, name, type, args, body):
        self.name = name
        self.type = type
        self.args = args
        self.body = body

class Arg:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Return:
    def __init__(self, value):
        self.value = value

class Block:
    def __init__(self, type, var_list, stmt_list):
        self.type = type
        self.var_list = var_list
        self.stmt_list = stmt_list

class Var:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value



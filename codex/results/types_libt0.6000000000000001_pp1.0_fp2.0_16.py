import types
types.ClassType = type

# --------------------------------------------------------------------
# Various exceptions used by the interpreter

class ExecutionError(Exception):
    def __init__(self, code_id, message, line=None, column=None):
        Exception.__init__(self, message)
        self.code_id = code_id
        self.line = line
        self.column = column

class ReturnedValue(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

class BreakLoop(Exception):
    def __init__(self, value=None):
        Exception.__init__(self)
        self.value = value

class ContinueLoop(Exception):
    pass

class StopIteration(Exception):
    pass

# --------------------------------------------------------------------
# The execution engine

class ExecutionEngine(object):
    def __init__(self, code_id, code, global_names, local_names,
                 filename=None, lineno=None, column=None):
        self.code_id = code_id
        self.code

from _struct import Struct
s = Struct.__new__(Struct)

class Instruction(object):
    def __init__(self, action, args, debugreg=None):
        self.action = action
        self.args = args
        self.debugreg = debugreg

    def __call__(self, frame):
        if self.action is not None:
            self.action(self, frame, *self.args)

    def __repr__(self):
        if self.debugreg is not None:
            return '%s(%r)' % (self.__class__.__name__, self.debugreg)
        elif self.args:
            return '%s(%r)' % (self.__class__.__name__, self.args)
        return self.__class__.__name__

class Const(Instruction): pass
class Store(Instruction): pass
class Load(Instruction): pass
class JumpIfTrue(Instruction): pass
class JumpIfFalse(Instruction): pass
class JumpAbsolute(Instruction): pass
class ReturnValue(Instruction): pass
class PopBlock(Instruction): pass

class Call

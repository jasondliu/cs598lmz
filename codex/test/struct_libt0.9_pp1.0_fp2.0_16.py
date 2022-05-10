import _struct

class SyscallObserver(OcsTranslatorObserver):
    __slots__ = ['syscall_des']

    def __init__(self, syscall_dereferencer=None, observer_objects=[]):
        OcsTranslatorObserver.__init__(self) 
        self.syscall_des = SyscallDereferencer() if syscall_dereferencer is None else syscall_dereferencer
        self.observers = observer_objects


    def function_enter(self, name, args):
        if name == 'syscall':
            code = self.syscall_des.dereference(args[0])
            syscall_name = self.syscall_des.lookup(code)
            for observer in self.observers:
                observer.syscall_enter(code, syscall_name, args[1:])
            return True
        return False


import mmap
# import pdb
# _pdb = pdb.Pdb(stdin=sys.__stdin__, stdout=sys.__stdout__)


class _Pdb(pdb.Pdb):
    """Override Pdb to use custom stdin and stdout"""

    def __init__(self, stdin=None, stdout=None, skip=None):
        pdb.Pdb.__init__(self, stdin, stdout)
        self.skip = set(skip) if skip else None

    def do_continue(self, arg):
        if self.curindex + 1 == len(self.stack):
            return 1
        else:
            return pdb.Pdb.do_continue(self, arg)

    def get_stack(self, f, t):
        stack, i = pdb.Pdb.get_stack(self, f, t)
        # pdb.set_trace()
        # _pdb.set_trace()
        return stack, i

    def get_stack_traceback(self, tb):
        # p

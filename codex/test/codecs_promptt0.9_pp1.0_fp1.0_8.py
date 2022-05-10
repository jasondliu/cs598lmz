import codecs
# Test codecs.register_error
read_stacks = 0
read_ecode_list = 0
ecode_max = 0
ecode_list = []

class Codec(codecs.Codec):
    def encode(self,input,errors='strict'):
        global read_stacks
        global read_ecode_list
        global ecode_max
        global ecode_list
        if errors != 'strict':
            read_stacks = sys._getframe().f_back.f_back
            read_ecode_list = True
            ecode_list = list(input)
            ecode_max = 2**15
            return ("*"*ecode_max).encode("utf-8"), ecode_max
        else:
            raise UnicodeEncodeError("bad", u"", 0, 1, "")

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return Codec().encode(input, self.errors)[0]


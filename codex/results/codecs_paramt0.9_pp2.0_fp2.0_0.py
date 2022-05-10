import codecs
codecs.register_error('backslashreplace', codecs.backslashreplace_errors)

from exceptions import IOError


class VT100(object):
    states=['START','ESCAPE','CSI','TITLE','ANSI','CSI_INTERMEDIATE','OSC']
    mode='START'
    buffer=[]
    ansi=[]
    csi_buffer=[]
    csi_args=[]
    csi_intermediate=''
    csi_final=''
    current_title=''
    title=[]
    osc_buffer=[]
    history=[]
    ident='envvy transport'
    s=''
    def __init__(self):
        self.transport = None
    
    def connection_made(self,transport):
        self.transport = transport
        self.buffer = []
        self.title=[]
        self.osc_buffer=[]
        self.current_title=''
        self.s=''
        self.send('\x1b]1;%s\x07' % self.ident)
       

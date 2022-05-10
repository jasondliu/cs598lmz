import _struct

def bbprobe_serialize(bb):
    """
    Convert a ProgramBlock.Probe() to a binascii string.
    """
    _s = StringIO()
    _s.write(_struct.pack('I', bb.id))
    _s.write(_struct.pack('I', bb.probeid))
    _s.write(_struct.pack('I', len(
        bb.disassembly
        )))
    _s.write(_struct.pack('I', len(
        bb.comments
        )))

    _s.write(_struct.pack(str(len(bb.disassembly)) + 's', bb.disassembly))
    _s.write(_struct.pack(str(len(bb.comments)) + 's', bb.comments))
    return _s.getvalue()

def bbprobe_deserialize(bbprobe_binary):
    """
    Convert a bbprobe_binary to a ProgramBlock.Probe()
    """
    _bb = ProgramBlock.Probe()
    _

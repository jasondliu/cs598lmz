import _struct

class SMB2CreateResponse_Parameters(Structure):
    structure = (
        ('StructureSize','<H=60'),
        ('OplockLevel','<B=0'),
        ('Reserved1','<B=0'),
        ('Reserved2','<H=0'),
        ('CreateAction','<I=0'),
        ('CreationTime','<Q=0'),
        ('LastAccessTime','<Q=0'),
        ('LastWriteTime','<Q=0'),
        ('ChangeTime','<Q=0'),
        ('AllocationSize','<Q=0'),
        ('EndofFile','<Q=0'),
        ('FileAttributes','<I=0'),
        ('Reserved','<I=0'),
        ('FileId','16s=""'),
    )

class SMB2CreateResponse(Structure):
    structure = (
        ('StructureSize','<H=9'),
        ('OplockLevel','<B=0'),
        ('Flags','<B=0'),
        ('CreateContextsOffset','<I=0'),
        ('Create

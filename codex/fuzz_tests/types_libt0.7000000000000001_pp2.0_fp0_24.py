import types
types.ModuleType
_getframe = types.FrameType.f_locals
types.FrameType.f_locals = new.instancemethod(_f_locals, None, types.FrameType)

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
CTYPES_MAPPING = {"C_STRING": ctypes.c_char_p}

def define_restype(return_type, use_yield_factory=True):
    """
        处理返回值以及包装 yield 的函数处理
    """
    fiber = False
    if "yield" in return_type:
        fiber = True
        return_type = return_type.replace(" yield", "")

    restype = CTYPES_MAPPING.get(return_type, None)
    if restype is None:
        try:
            restype = getattr(CTYPES_MAPPING["C_STRING"], return_type)
        except AttributeError as e:
            print("没有找到 {} 类型的封装".format(return_type))
            # TODO: 通过检测系统是否

import _struct

class _CDataMeta(type):
    def __new__(self, name, bases, dict):
        tp_dict = dict.get('__typedict__', None)
        if tp_dict is None:
            return super(_CDataMeta, self).__new__(self, name, bases, dict)
        if not isinstance(tp_dict, dict):
            raise TypeError("invalid __typedict__ attribute")
        # Generate the right C type, depending on the layout requested.
        # We ignore all other options (packing, alignment...)
        # XXX this is not really PEP-7 compliant
        s = "struct %s_s { " % name
        for (attr_name, tp) in tp_dict.items():
            s += "%s %s; " % (tp, attr_name)
        s += "}"
        source = "typedef %s %s;" % (s, name)
        d = {}
        # Generate a w_type
        w_type = interp_cpy_gcc.generate

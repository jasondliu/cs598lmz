import _struct_repr as _struct_repr
        _tmp_tst = _struct_repr.Struct('test')
        _tmp_tst.add(['type',     ctypes.c_char * 4])
        _tmp_tst.add(['sint',     ctypes.c_int])
        _tmp_tst.add(['sint_arr',  ctypes.c_int * 16])
        _tmp_tst.add(['double',   ctypes.c_double])

        self.tmp_tst = _tmp_tst

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #! THIS IS SO IMPORTANT, THERE IS A BUG IN CPYTHON WITH 64-BIT LINUX SYSTEMS
        #! THE BUG ALLOWS FOR MULTIPLE REFERNCES TO THE SAME REFERENCE COUNTED
        #! OBJECT IN A CTITES STRUCTURE (except if a reference to the object is
        #! passed in as a keyword argument to a structure or union constructor,
        #! or if the keyword argument is used when

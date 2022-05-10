import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)


class PGCon(object):
    """todo
    
    
    Attributes:
        ERROR             -- title,.
        WARNING           -- title,.
        NOTICE            -- title,.
        author            -- title,.
        title             -- title,.
        size              -- title,.
        args              -- title,.
        keys              -- title,.
        newtitle          -- title,.
        newauthor         -- title,.
        DB                -- title,.
        ulist             -- title,.
        finput            -- title,.
        lineno            -- title,.
        cache             -- title,.
        func_p            -- title,.
        func_n            -- title,.
        next_p            -- title,.
        prev_p            -- title,.
        prev_n            -- title,.
        _c                -- title,.
        _c_next           -- title,.
        _c_prev           -- title,.
        _cur              -- title,.
        _id               -- title,.
        TIME              -- title,.
        re_ssn            -- title,.
        add_ssn           -- title,.
        get_next          -- title

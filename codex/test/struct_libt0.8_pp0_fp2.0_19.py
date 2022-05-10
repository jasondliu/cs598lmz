import _struct

_SYS_SIGLIST_DUMMY = {}

def _sys_siglist():
    if 'siglist' in _SYS_SIGLIST_DUMMY:
        return _SYS_SIGLIST_DUMMY['siglist']

    if _ctypes:
        _sig_num_to_name_dict = dict(
            _signal.__dict__)
        _sig_num_to_name_dict.update(
            _signal.__dict__.get('__xload', {}))

        sig_num_to_name = {}
        for k, v in _sig_num_to_name_dict.items():
            if isinstance(v, int):
                sig_num_to_name[v] = k.upper().replace('SIG', '')

        res = [None] * (max(sig_num_to_name)+1)

        for k, v in sig_num_to_name.items():
            res[k] = v


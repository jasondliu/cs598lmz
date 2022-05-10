import codecs
codecs.register_error('strict', codecs.ignore_errors)

def dict_from_rq_get(rq_get, limit=None):
    gdict = copy.copy(rq_get)
    limits = []
    for rk in gdict.keys():
        rv = gdict.get(rk)
        try:
            rv = codecs.escape_decode(rv)[0].decode('latin-1')
            if '|' in rv:
                rv = rv.split('|')
                for n, v in enumerate(rv):
                    try:
                        rv[n] = int(v)
                    except:
                        pass
            else:
                try:
                    rv = int(rv)
                except:
                    pass
        except:
            rv = None
        gdict[rk] = rv
        if rk.startswith('limit_'):
            limits.append(rk)
    if 'limit_0' in limits:
        limit = gdict.get('limit_0')

import lzma
lzma.decompress

import json
try:
    from . import funcs as f
except:
    import funcs as f

data = open('../data/fusion_data','rb').read()
data = data.split(b'\r\n')
data = [d.split(b'\t') for d in data]
data = [('{}_{}'.format(d[-2].decode(), d[-1].decode()), d[1].decode()) for d in data]
data = [d for d in data if d[1] != 'None']
data = [d for d in data if d[1] != 'null']
data = [(d[0], json.loads(d[1])) for d in data]
genes = [d[0] for d in data]
genes = [g.split('_') for g in genes]
genes = [(g[0], g[1]) for g in genes]
genes = [g for g in genes if g[0] != g[1]]
genes = [('{

from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'QQQQQQQQ'
s.size = struct.calcsize(s.format)

def build_map(fpath):
    node = {}
    q = []

    with open(fpath, 'rb') as f:
        while True:
            d = f.read(s.size)
            if not d:
                break

            if len(d) < s.size:
                continue

            pn, nn, pv, nv, pn_n, nn_n, pv_n, nv_n = s.unpack(d)
            q.append((pn_n, nn_n, pv_n, nv_n))

        while q:
            pn, nn, pv, nv = q.pop()
            if nn not in node:
                node[nn] = {}
            if pn not in node:
                node[pn] = {}
            node[nn][pn] = True
            node[pn][nn] = True

            q.append((pn

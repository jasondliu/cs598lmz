import _struct

def write_obj(filename, verts, uvs, norms, faces):
    f = open(filename, 'w')
    verts = [str(v).encode('ascii', errors='ignore') for v in verts]
    faces = [[str(v) for v in f] for f in faces]
    for v in verts:
        f.write('v ' + str(v) + '\n')
    for vt in uvs:
        f.write('vt ' + str(vt) + '\n')
    for vn in norms:
        f.write('vn ' + str(vn) + '\n')
    for ff in faces:
        f.write('f ')
        for f in ff:
            f.write(str(f) + ' ')
        f.write('\n')
    f.close()

def write_mhx(filename, verts, faces, mods=[], uvs=[], grups=[], mats=[], revnorm=False, subds=[], tessds=[], donorm

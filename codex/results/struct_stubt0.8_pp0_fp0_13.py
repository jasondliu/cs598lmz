from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<I')  # 'I' stands for unsigned int (4 bytes)

def verts_to_tris (verts, faces):
    ''' Converts verts to tris.
    '''
    return [tuple(verts[v] for v in face) for face in faces]

def tris_to_verts (tris):
    ''' Converts tris to verts.
    '''
    verts = []
    for tri in tris:
        for vert in tri:
            verts.append(vert)
    return verts

def remove_duplicate_verts (verts):
    ''' Removes duplicate vertices from a list of vertices.

        verts: A list of (x, y, z) vertices.
    '''
    verts = set(verts)
    return [list(vert) for vert in verts]

def remove_duplicate_tris (tris):
    ''' Removes duplicate triangles from a list of triangles.

        tris: A list of (x, y,

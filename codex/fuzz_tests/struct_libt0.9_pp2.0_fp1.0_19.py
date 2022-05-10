import _struct_2_mfem_mesh as smesh
 
import numpy as np

def update_mfem_struct(mesh):
    h = mesh.GetElementTransformation(0).GetB()
    s = np.zeros([h.Height(), h.Width()], dtype=np.float64, order="F")
    for j in xrange(h.Width()):
        for i in xrange(h.Height()):
            s[i,j] = h(i,j)
    mesh.struct = h

    # compute coordinates of barycenter
    bc = np.zeros([mesh.GetNE(),3], dtype=np.float64, order="F")
    reference = np.zeros([3,3], dtype=np.float64, order="F")
    reference[0,0] = 1
    reference[1,1] = 1
    reference[2,2] = 1
    for i in xrange(mesh.GetNE()):
        h = mesh.GetElementTransformation(i).GetB()
        bc

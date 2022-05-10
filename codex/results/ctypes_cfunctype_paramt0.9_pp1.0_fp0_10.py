import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
gSOYSA_F = FUNTYPE(("SOYSA_F", SPlib))



#MEHSSA
MEHSSA_F = FUNTYPE(("MEHSSA_F", SPlib))

#FSHSA
FSHSA_F = FUNTYPE(("FSHSA_F", SPlib))

S_Rubby = FUNTYPE(("S_Rubby", SPlib))


#soybean
def SOYSA(t1,t2,t3,t4,t5,t6,t7,DIJ,t9,t10,t11,t12):
    DIJ = numpy.array(DIJ)
    soytraits = numpy.array(

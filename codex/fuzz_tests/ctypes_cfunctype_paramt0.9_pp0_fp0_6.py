import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    c_int, c_int, c_int, c_int, c_int, c_int, c_void_p
)
CGAL_DS3_CYCLE_BREAKING_POLICY = FUNTYPE(
    return_CGAL_DS3_CYCLE_BREAKING_POLICY
)
CGAL_DS3_STRATEGY_POLICY = FUNTYPE(
    return_CGAL_DS3_STRATEGY_POLICY
)
CGAL_DS3_STRATEGY_OBJECT = POINTER(CGAL_DS3_STRATEGY_POLICY_TAG)
CGAL_DS3_STRATEGY = POINTER(CGAL_DS3_STRATEGY_POLICY)

# Delaunay triangulation dD functions
class DS3_Delaunay_Triangulation_d(Structure):
    pass

Delaunay_triangulation_d = DS3_Delaunay_Triangulation_d
DS3_Delaunay_Triangulation_d_create = dso.new_Delaunay

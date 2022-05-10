import types
types.traceback.print_exception(*exc)
print("==================================")
np.set_printoptions(precision=4)
roundtrip(np.array([np.inf]), get_val=lambda x: float(x))
roundtrip(np.array([-np.inf]), get_val=lambda x: float(x))
print("==================================")
roundtrip(np.array([np.inf]).reshape(1,1), get_val=lambda x: float(x))
print("==================================")
roundtrip(np.array([-np.inf]).reshape(1,1), get_val=lambda x: float(x))
print("==================================")
roundtrip(np.array([np.inf]).reshape(1,1,1), get_val=lambda x: float(x))
print("==================================")
roundtrip(np.array([-np.inf]).reshape(1,1,1), get_val=lambda x: float(x))
print("==================================")
for D in [1, 2, 3]:
    inf = np.full((1,)*D

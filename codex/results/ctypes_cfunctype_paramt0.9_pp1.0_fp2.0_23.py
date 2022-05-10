import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_double,
                           ctypes.c_double, ctypes.c_double)
#set_f = FUNTYPE(set_f)
set_f = FUNTYPE(flame.set_function)

#create ODE system
ode = ffi.gc(flame.dense_output_CIR_Ode(a, b, sigma, set_f, n),
             flame.dense_destroy_CIR_Ode)

#create solver object
algorithm = ffi.gc(flame.rk78_dopri5_create(ode), flame.rk78_dopri5_destroy)

#initialize solver
flame.rk78_dopri5_initialize_solver(algorithm, float(T0), int(M), float(tol))

#solve ODE
flame.rk78_dopri5_solve(algorithm)

#get solution
sol = ffi.gc(flame.rk78_dopri5_get_result(

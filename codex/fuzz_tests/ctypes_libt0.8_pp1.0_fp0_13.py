import ctypes
ctypes.CDLL('/Applications/MATLAB_R2016a.app/bin/maci64/libtbb.dylib')

# change the path below
sys.path.append('/Applications/MATLAB_R2016a.app/extern/engines/python/dist/matlab/engine/examples')
import matlab.engine

eng = matlab.engine.start_matlab()
%%time
eng.mexfun(nargout=0)

# put your function name after mexfun

eng.quit()

M = np.random.rand(1000,1000)
M.shape
%%time
M.sum()
%%time
M.mean()
%%time
M.std()
%%time
M.var()
%%time
M.dot(M.T)
%%time
M.max()
%%time
M.min()
%%time
np.dot(M,M.T)

 

%%time
eng.mexfun(nargout=0)

# put your function name after mexfun

eng.quit()
M =

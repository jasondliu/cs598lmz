import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(structures.Residue), ctypes.POINTER(structures.Residue), ctypes.c_double)
self._pyPFunction = FUNTYPE(PyPFunction)
pf = structures.PFunction(self._pyPFunction, self.THR_FAC, self._pyRes, self._pyRes)
```
## Make and Run
```bash
cd $ROOT
mkdir build
cd build
cmake ..
make
# run test
#./CTest
```

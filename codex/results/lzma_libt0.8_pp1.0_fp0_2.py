import lzma
lzma_default = lzma.LZMAFile('/home/sbragagnini/Projects/RF-LAMMPS/src/lammps/SRC/lzma_default')
lzma_mayor_par = lzma.LZMAFile('/home/sbragagnini/Projects/RF-LAMMPS/src/lammps/SRC/lzma_default_mayor_par')
lzma_mayor_par.seek(0)
lzma_mayor_par_content = lzma_mayor_par.read()
lzma_default_content = lzma_default.read()
lzma_default.seek(0)
lzma_default.seek(0)
lzma_mayor_par.seek(0)

def get_iterations(fileobject):
    iterations = []
    for line in fileobject:
        if line.startswith('Step Temp'):
            iteration_line = line.split()
            iteration = iteration_line[1]
            iterations.append

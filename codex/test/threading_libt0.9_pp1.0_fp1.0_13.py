import threading
threading.stack_size(1024*1024)

pdb_file = "/mnt/d/ISB/Data/abx000/md.part0001.gro"
rna_file = "/mnt/d/ISB/Code/Users/Nail/general-analysis/b-dna-analysis/rna.hdf5"
msm_out_file = "/mnt/d/GB/Users/Nail/Simulation_Data/msm/msm.hdf5"
dihedrals_file = "/mnt/d/GB/Users/Nail/Simulation_Data/msm/dihedrals.hdf5"

torsion_indices = [3, 5, 7, 9]
sampling_frequency = 10

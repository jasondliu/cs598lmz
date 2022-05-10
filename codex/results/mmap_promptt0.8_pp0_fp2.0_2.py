import mmap
# Test mmap.mmap performance when reading and writing data back and forth
m = mmap.mmap(0, 100) # size is 100 bytes
m[10:20] = b'1234567890'
m[10:20]

# There are two ways to implement MIMO: 1) Eigenvalue decomposition; 2) Givens rotation.
# Reference: https://en.wikipedia.org/wiki/Multiple_input_multiple_output
# We will use the QR decomposition version
# The paper in the reference sectio gives a very detailed explanation of how to implement the Givens rotation version
# Reference: https://www.cs.ucsb.edu/~kfisler/pubs/kfisler-globecom09.pdf

 
# Helper functions

def eigenvalue_decomposition(mat):
    # Return the eigenvalue vectors and eigenvalue matrices
    eigenvalues, eigenvectors = np.linalg.eig(mat)
    return eigenvalues, eigenvectors

def qr_decomposition(mat):
    # Return the orthog

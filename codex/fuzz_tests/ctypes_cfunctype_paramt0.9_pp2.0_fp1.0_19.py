import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_longdouble)
@FUNTYPE
def ui(l):
    return math.log10(l)
def log(x):
    if abs(x) < 1:
        return x.dot(x)
    else:
        return ui(x)

print(log(np.linalg.norm(data)))
'''

big_cov_matrix = np.cov(data.T)

w, v = np.linalg.eig(big_cov_matrix)

# sort eigenvalues and eigenvector
#decending order
sort_indices = np.argsort(w)[::-1]
w = w[sort_indices]
v = v[:, sort_indices]

print(w)

#scale the data
#data = 2 * data

#decompose
v_t = np.transpose(v)
data_new = np.dot(v_t, data)
print(data_new)

#plot
plt.

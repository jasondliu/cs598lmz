import socket
socket.if_indextoname(2)

# %%
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

np.concatenate((a,b), axis=1)

# %%
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

np.concatenate((a,b), axis=0)

# %%
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

np.vstack((a,b))

# %%
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

np.hstack((a,b))

# %%
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])


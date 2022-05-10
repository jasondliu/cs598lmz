import ctypes
ctypes.cast(int(((a.tolist()).index(max(a.tolist()))))/5, ctypes.c_int)

# %%
b = np.zeros(m)
b[0] = max(a.tolist())
for i in range(1, m):
    q = np.zeros(n-i*5)
    for j in range(n-i*5):
        q[j] = max(a[j:j+5])
    b[i] = max(q)

# %%

y = np.zeros(m)
for i in range(m):
    y[i] = (b[i]-b[i-1])/b[i]

# %%

import matplotlib.pyplot as plt
# plt.plot(np.linspace(0, n, n), a, 'b')
# plt.plot(np.linspace(5, n, m), b, 'g')
plt.plot(np.linspace(5, n, m), y, 'r')

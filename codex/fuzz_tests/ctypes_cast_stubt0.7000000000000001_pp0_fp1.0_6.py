import ctypes
ctypes.cast(ptr, ctypes.py_object).value

# <codecell>

for i in range(N):
    print ptr[i]

# <codecell>

arr = np.arange(5)
print arr
d_arr = cuda.to_device(arr)
d_arr.copy_to_host()

# <codecell>

print arr

# <codecell>

x = np.linspace(0,10,1000)
y = np.sin(x)

X,Y = np.meshgrid(x,y)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.plot_surface(X,Y,np.exp(X)*y)

plt.show()

# <codecell>

x = np.random.randn(100,100)

plt.hist(x)
plt.show()

# <codecell>

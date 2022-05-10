import socket
socket.if_indextoname(8)

out = vizmat.fig2data(fig)
out.shape
print("PNG size  = {0}".format(out.shape))
print("JPG size  = {0}".format(out.shape))
print("BMP size  = {0}".format(out.shape))

X,Y = np.meshgrid(seq(0,1,0.1),seq(0,1,0.1))
Z = peaks(X,Y)
fig = vizmat.figure(figsize=(8,8))
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=vizmat.cm.rainbow)
ax.set_zlim(0,8)


x = np.linspace(0, 1, 50)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
fig = vizmat.figure()
ax = fig.add_subplot(211)
ax.plot

import lzma
lzma.decompress(open('../data/train/x_train_rgb_0.npy.lzma', 'rb').read())

x_train_rgb = np.zeros((num_train, 32, 32, 3))
for i in range(num_train):
    x_train_rgb[i, ...] = np.load('../data/train/x_train_rgb_%d.npy' % i)
x_train_rgb = np.reshape(x_train_rgb, (num_train, -1))

x_train_hsv = np.zeros((num_train, 32, 32, 3))
for i in range(num_train):
    x_train_hsv[i, ...] = np.load('../data/train/x_train_hsv_%d.npy' % i)
x_train_hsv = np.reshape(x_train_hsv, (num_train, -1))

x_train_lab = np.zeros((num_train, 32,

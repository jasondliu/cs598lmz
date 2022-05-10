import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

x = np.arange(-10, 10, 0.01)
y = np.sinc(x)

plt.plot(x, y)

plt.show()


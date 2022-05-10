import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

data = np.loadtxt('data.txt')
xdata = data[:,0]
ydata = data[:,1]

def gauss_fit(x, A=1., mu=0., sig=1.):
    return A*np.exp(-(x-mu)**2/(2*sig**2))

def fit_gauss(x, y, A=1., mu=0., sig=1.):
    # Define our objective function
    def objective(params):
        return np.sum((y-gauss_fit(x, *params))**2)
    # Define the initial guess
    p0 = [A, mu, sig]
    # Fit the data
    result = scipy.optimize.minimize(objective, p0)
    # Return the result
    return result.x

# Fit the data
params = fit_gauss(xdata, ydata)

# Make some data for the fit
xfit = np.linspace(xdata.min(), xdata

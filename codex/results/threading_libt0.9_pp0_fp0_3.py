import threading
threading.stack_size(1000000)

nc=150
meth='exp'
sigma_g=2.5
branch=0
n_train=100

total_sigmas=np.array([[3.0,2.5,2.0],
                       [3.0,2.5,2.0],
                       [1.5,1.0,0.5]])

total_lambdas=np.array([[0.5,1.0,1.5],
                       [0.5,1.0,1.5],
                       [0.5,1.0,1.5]])

total_alphas=np.array([[3.0,2.5,2.0],
                       [3.0,2.5,2.0],
                       [1.5,1.0,0.5]])

total_gammas=np.array([[1.5,1.0,0.5],
                       [1.5,1.0,0.5],
                       [1.5,1.0

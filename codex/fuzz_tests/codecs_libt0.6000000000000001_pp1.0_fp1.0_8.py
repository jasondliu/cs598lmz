import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

#Useful for adding to the folder name if you want to save multiple runs
#Change it to anything you want, or just empty string if you don't want to use it
run_id = '_final'

#This is the main experiment parameters
class Exp_params:
    def __init__(self):
        #The following four parameters are important ones, the rest are less important
        self.k = 100 #The number of nearest neighbors
        self.radius = 0.5 #Radius
        self.min_ll_impr = 0.01 #Minimum log-likelihood improvement in M-step
        self.min_num_hits_for_hit_rate = 50 #Minimum number of hits in the validation set to consider the hit rate in the stopping criteria
        #The following are less important parameters, usually you can just leave their default values
        self.max_iters = 100 #The maximum number of iterations
        self.min_num_hits = 50 #Minimum number of hits in the validation set

import threading
threading.stack_size(2*1024*1024)

import gc
gc.collect()

#stat-test-003 작성.

######################################################################
#seed setting
def init_seed(seed):
    if seed is None:
        seed = random.randint(1,100000)
    random.seed(seed)
    np.random.seed(seed)
    if (gpu != 'None'):
        torch.cuda.manual_seed_all(seed)
    torch.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    os.environ['PYTHONHASHSEED'] = str(seed)
    return seed

######################################################################
#Experiment Focal Loss
focal_loss = False

######################################################################
#Image Generator

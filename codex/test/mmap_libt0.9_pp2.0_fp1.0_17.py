import mmap
from termcolor import colored

bar_length = 40


def save_checkpoint(model, filename):
    torch.save(model.state_dict(), filename)


def save_config(config, filename):
    with open(filename, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)


class AverageMeter(object):
    """Computes and stores the average and current value"""

    def __init__(self):
        self.val = 0
        self.avg = 0
        self.sum = 0

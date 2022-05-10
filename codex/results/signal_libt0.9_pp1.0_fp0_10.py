import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from tqdm import tqdm
# Counts number of cells hit in all shots without stiching
class Counter(object):

    def __init__(self):
        self.cells_hit = {}
        self.total = 0
        self.coverage = 0

    def count(self, config_list, query, new_cells):
        for cell in new_cells:
            if cell not in self.cells_hit:
                self.cells_hit[cell] = config_list

        if self.total == 0:
            self.total = query.num_cells

        self.coverage = len(self.cells_hit) / self.total    
    
    def report(self):
        print(self.coverage, self.total, len(self.cells_hit))

def main():
    env = create_env(mode='human')
    model = initialise_model(env.action_space)
    log_dir = 'data/logs/'
    writer = Summary

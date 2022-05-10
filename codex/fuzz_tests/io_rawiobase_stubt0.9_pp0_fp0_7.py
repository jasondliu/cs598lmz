import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return super().read(n)

class Logger:
    def __init__(self,name=None,json=False, output_file=False):
        self.name = name
        self.json = json
        self.output_file = output_file
        self.reset()
 
    def reset(self):
        if self.output_file:
            self.log_file = open('logs/{}.txt'.format(self.name), 'w')
            self.log_file.write('')
            self.log_file.close()
        self.iter = 0
        self.all_losses = np.array([])
        self.loss_dict={}
        self.log_dict={}
        self.log_dict['x'] = []
        self.log_dict['y'] = []
        for i, name in enumerate(Y_TASKS):
            self.log_dict[name] = []
 
        self.log_dict['std'] = []
        self.log

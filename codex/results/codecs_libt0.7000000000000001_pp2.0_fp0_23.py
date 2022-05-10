import codecs
codecs.register_error('replace2', codecs.replace_errors)

class Multitasking:
    def __init__(self, func):
        self.func = func
        self.threads = []
        pass

    def add_job(self, *args, **kwargs):
        self.threads.append(Thread(target=self.func, args=args, kwargs=kwargs))
        pass

    def run(self):
        for t in self.threads:
            t.start()
        for t in self.threads:
            t.join()
        pass

def pre_process(input_dir, output_dir, dataset_name):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if dataset_name == 'yelp':
        pre_process_yelp(input_dir, output_dir)
    elif dataset_name == 'imdb':
        pre_process_imdb(input_dir, output_dir)
    else:
        print('unknown dataset

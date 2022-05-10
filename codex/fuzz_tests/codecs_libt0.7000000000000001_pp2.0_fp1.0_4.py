import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class Training:
    def __init__(self, name, data_root, num_of_epochs, batch_size, content_size,
                 style_size, num_of_workers, content_layer, style_layer,
                 content_weight, style_weight, tv_weight, learning_rate,
                 momentum, decay, resume, start_epoch, cuda, log_interval,
                 save_model):

      self.name = name
      self.data_root = data_root
      self.num_of_epochs = num_of_epochs
      self.batch_size = batch_size
      self.content_size = content_size
      self.style_size = style_size
      self.num_of_workers = num_of_workers
      self.content_layer = content_layer
      self.style_layer = style_layer
      self.content_weight = content_weight
      self.style_weight = style

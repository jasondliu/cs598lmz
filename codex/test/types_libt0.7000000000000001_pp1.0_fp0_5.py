import types
types.SimpleNamespace

class Config:
    def __init__(self):
        self.batch_size = 1
        self.train_data_dir = "/home/bohuang/Desktop/work/data/saiapr_tc/train/"
        self.train_label_dir = "/home/bohuang/Desktop/work/data/saiapr_tc/train_mask/"
        self.test_data_dir = "/home/bohuang/Desktop/work/data/saiapr_tc/test/"
        self.test_label_dir = "/home/bohuang/Desktop/work/data/saiapr_tc/test_mask/"
        self.total_epoch = 150
        self.input_height = 224
        self.input_width = 224
        self.train_info_file = "train_info.txt"
        self.test_info_file = "test_info.txt"
        self.model_dir = "./model/resnet50_224/"
        self.model_name = "resnet50"

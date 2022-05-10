import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

TRAIN_DATA_PATH = './data/caption/train/'
VAL_DATA_PATH = './data/caption/val/'
TEST_DATA_PATH = './data/caption/test/'

VGG_MODEL_PATH = "./data/vgg16.model"

if __name__ == '__main__':
    from data.data_loader import get_loader
    from solver import CaptioningSolver

    train_data_loader = get_loader(data_path=TRAIN_DATA_PATH,
                                   batch_size=128,
                                   shuffle=True)

    val_data_loader = get_loader(data_path=VAL_DATA_PATH,
                                 batch_size=128,
                                 shuffle=False)

    test_data_loader = get_loader(data_path=TEST_DATA_PATH,
                                  batch_size=128,
                                  shuffle=False)

    solver = CaptioningSolver(

import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

from model import Model
from config import FLAGS
import utils
import pickle

def main(_):
    print(FLAGS.__flags)

    # utils.export_ckpt(FLAGS.ckpt_path)

    choice = FLAGS.mode.lower()
    model = None
    if choice == 'train':
        model = Model(FLAGS)
    elif choice == 'test':
        model = Model(FLAGS)
        model.load()
    elif choice == 'back':
        model = Model(FLAGS)
        model.load()
    elif choice == 'chat':
        model = Model(FLAGS)
        model.load()
    elif choice == 'export':
        model = Model(FLAGS)
        model.load()
    else:
        raise ValueError("Unknown run mode. Only train/test/back/chat modes are supported.")

    model.run()

if __name__ == '__

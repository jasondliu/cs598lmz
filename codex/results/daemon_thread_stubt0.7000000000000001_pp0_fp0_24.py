import sys, threading

def run():
    args = sys.argv[1:]

    if '--help' in args:
        print('Usage: python main.py [OPTIONS]')
        print('')
        print('Options:')
        print('  --help               show this help message and exit')
        print('  --train              train a new model')
        print('  --predict            predict with a pre-trained model')
        print('  --dataset-path       path to folder containing dataset')
        print('  --model-path         path to output folder for model')
        print('  --epochs             number of epochs to train for')
        print('  --batch-size         batch size for training')
        print('  --img-size           image size for training')
        print('  --lr                 learning rate for training')
        print('  --n-classes          number of classes to classify')
        print('  --use-gpu            use gpu for training (default false)')
        return

    dataset_path = None
    model_path = None
    epochs = None
    batch_size =

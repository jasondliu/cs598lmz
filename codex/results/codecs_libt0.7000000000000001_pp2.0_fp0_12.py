import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

parser = argparse.ArgumentParser()
parser.add_argument('--input_path', type=str, help='Path to input video.')
parser.add_argument('--output_path', type=str, help='Path to output video.')
parser.add_argument('--model_dir', type=str, help='Path to model directory.')
parser.add_argument('--result_dir', type=str, help='Path to result directory.')
parser.add_argument('--fps', type=int, default=30, help='FPS of the output video.')
parser.add_argument('--model_type', type=str, default='resnet', help='Model type.')
parser.add_argument('--model_name', type=str, default='resnet_v2_50', help='Model name.')
parser.add_argument('--n_classes', type=int, default=3, help='Number of classes.')
parser.add_argument('

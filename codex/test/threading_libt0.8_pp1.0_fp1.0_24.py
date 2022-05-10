import threading
threading.stack_size(1024 * 1024 * 1024 * 2)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--input_list",
    default="",
    type=str,
    required=True,
    help="The input images list.")
parser.add_argument(
    "--input_dir",
    default="",
    type=str,
    required=True,
    help="The input images directory.")
parser.add_argument(
    "--output_dir",
    default="",
    type=str,
    required=True,
    help="The output directory.")
parser.add_argument(
    "--data_format",
    default="NHWC",
    type=str,
    required=False,
    help="Data layout format.")
parser.add_argument(
    "--batch_size",
    default=1,
    type=int,
    required=False,
    help="The batch size.")

import mmap
import os

from new_footer import new_footer

from PIL import Image
import rawpy
import typer

from modules.data_processing import extract_exifdata, get_date_modified_from_exif_data
from modules.directory_maintenance import get_file_list
from modules.ipyfilechooser import FileChooser


def run_rawpy(img_path: str):
    """Use RawPy to convert given path to TIF

    Args:
        img_path (str): Image path
    """

    with rawpy.imread(img_path) as raw:
        rgb = raw.postprocess(use_auto_wb=True, gamma=(1, 1), no_auto_bright=True, output_bps=16)
    new_img_name = os.path.splitext(img_path)[0] + ".tif"
    new_img = Image.fromarray(rgb)

from bz2 import BZ2Decompressor
BZ2Decompressor.flush = MagicMock(name='flush')

from jicbioimage.core.io import FileBackend
from jicbioimage.core.image import Image
from jicbioimage.core.transform import transformation
from jicbioimage.core.transform import identify_regions

from jicbioimage.transform import (
    invert,
    scale,
    remove_small_objects,
    threshold_otsu,
    select_regions,
    erode_binary,
    dilate_binary,
    skeletonise,
    binarize,
    median_filter,
    _mark_edges,
)


# @unittest.skip("temporarily disabled")
class TestFilters(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestFilters, self).__init__(*args, **kwargs)

    def setUp(self):
        self.image = Image.from_file(join(input_data_dir, 'uniform.png'))
        self.

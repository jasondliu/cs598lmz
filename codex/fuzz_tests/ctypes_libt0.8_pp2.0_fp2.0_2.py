import ctypes
ctypes.cdll.LoadLibrary('libcaffe2_detectron_ops_gpu.so')
# sys.path.insert(0, python_lib)
print('import detectron')
# from detectron.core.config import assert_and_infer_cfg
# from detectron.core.config import cfg
# from detectron.core.config import merge_cfg_from_file
# from detectron.utils.io import cache_url
# from detectron.utils.logging import setup_logging
# from detectron.utils.timer import Timer
# import detectron.core.test_engine as infer_engine
# import detectron.datasets.dummy_datasets as dummy_datasets
# import detectron.utils.c2 as c2_utils
import detectron.utils.vis as vis_utils

c2_utils = os.path.join(ROOT_DIR, 'detectron', 'utils', 'c2')
print(c2_utils)
# assert os.path.exists(c2_utils), 'Cannot find c2_utils.

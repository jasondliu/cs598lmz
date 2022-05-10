from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('../data/en.wiki.bz2','r').read())

from smart_open import smart_open
import bz2
f=bz2.BZ2File('../data/en.wiki.bz2')
launch = Launch(config=config)
launch.register(
    name='xml_parsing',
    module_file=os.path.abspath('./parse_xml.py'),
    args=['--log-file-prefix', os.path.abspath('parse_xml.log')],
    config={},
    job_config={},
    tags={}
)

launch.register(**(launch.start_local_cluster(
    num_cpus=2,
    num_gpus=0,
    resources={'extra_cpu':4},
    webui_host='0.0.0.0'
)))

launch.wait()
launch.block()
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession


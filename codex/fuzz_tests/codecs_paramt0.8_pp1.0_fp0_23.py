import codecs
codecs.register_error('strict', codecs.ignore_errors)
codecs.register_error('ignore', codecs.ignore_errors)

from pynwn.file.gff import GFF
from pynwn.file.utc import UTC
from pynwn.file.dlg import DLG
from pynwn.file.utt import UTT
from pynwn.file.utt import UTT_Entry
from pynwn.file.tlk import TLK
from pynwn.file.bif import get_ifo, get_res

logging.basicConfig(format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)

def get_store(gff_path, bif_paths):
    bif_filenames = []
    for path in bif_paths:
        bif_filenames.extend(glob.glob(os.path.join(path, '*.bif')))

    if bif_filenames == []:
        raise Exception('No BIF files found

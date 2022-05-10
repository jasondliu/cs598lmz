import codecs
codecs.register_error('strict', codecs.ignore_errors)

sys.path.insert(0, CFG_BINDIR + '/sbin/retrieve_ead')
from get_pid_from_recid import main as ead_get_pid_from_recid
from get_record_infos import main as ead_get_record_infos

if sys.stdout.encoding == 'UTF-8':
    logging_encoding = 'utf-8'
else:
    logging_encoding = 'iso8859-1'

class EADDownloader(XMLDownloader):
    """
    Downloader for the EAD metadata format
    """
    recid_xpath = '/ead:ead/ead:eadheader/ead:eadid'
    md_format = 'EAD'

    def __init__(self, *args, **kwargs):
        """Init method"""
        XMLDownloader.__init__(self, *args, **kwargs)
        self.ea_recid = None
        self.ea_pid = None
        self.ea_maindata

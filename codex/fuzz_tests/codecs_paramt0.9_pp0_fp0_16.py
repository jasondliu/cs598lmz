import codecs
codecs.register_error('strict', codecs.ignore_errors)

logger = logging.getLogger(__name__)

_MAIL_SETTINGS_FILE = None
_IMAP_SETTINGS = None
_USE_TLS = False
_VALIDATE_SSL_CERT = True
_local_mailboxes = None
_FOLDERS_TO_MONITOR = []

def _local_folder_name(email):
    folder = email.get_header(FROM_HEADER,'no_from').replace('/','_')
    email._local_folder_name = folder
    return folder

def close():    
    global _local_mailboxes
    if _local_mailboxes:
        for (mailbox, connection) in _local_mailboxes.values():
            connection.close_folder()
        _local_mailboxes.clear()
    logging.debug("Email Client Closing")

def open_local_folder(email):
    global _local_mailboxes
    if not _local_mailboxes:
        _local_mailboxes = {}
    folder_name =

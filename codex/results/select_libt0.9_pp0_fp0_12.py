import selectors
import socket
import threading
import time
import types

HTTP_CONNECT_TIMEOUT = 20

DL_LIMIT = json.loads(os.environ['DT_TENANT_OPTIONS'])['download_limit'] * 1024 * 1024
UL_LIMIT = json.loads(os.environ['DT_TENANT_OPTIONS'])['upload_limit'] * 1024 * 1024

logger = logging.getLogger('upload.s3')


def encode_utf8(value: str) -> str:
    """
    S3 key names don't like unicode characters, and we don't want them in our data storage.
    """
    return str(value)


class S3Connector:
    """
    This connector uses the aws python boto library to connect and communicate with S3.
    """

    def __init__(self, s3_cfg: dict):
        self.s3_cfg = s3_cfg
        self.s3_client = boto3.client('s3',
                                      aws_access_key

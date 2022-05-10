import weakref

from arrowhead_client.exceptions import UnauthorizedError
from arrowhead_client.http import HttpConsumerClient
from arrowhead_client.requests import Auth
from tests.http.mock import HttpClientMock

ARROWHEAD_URL = "http://localhost:12345"


@pytest.fixture(scope="module")
def consumer_client():
    consumer_client = HttpConsumerClient(ARROWHEAD_URL)
    consumer_client.auth = Auth()
    consumer_client.auth.certificate = {
        "version": 3,
        "serial_number": "0A:B5:A3:85:A5:CD:72:D6:F2:34:C9:08:A8:7A:A5:93",
        "signature_algorithm": "sha256WithRSAEncryption",
        "issuer": {
            "organization_name": "Acme Co Inc."
        },
        "subject": {
            "common_name": "httpconsumer"
        },
        "not_valid_before": "

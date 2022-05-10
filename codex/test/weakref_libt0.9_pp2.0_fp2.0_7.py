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

import weakref

from kokki import Environment, Fail, Service
from kokki.cookbooks.apache2.resources import VirtualHost

class TestApache2Resource(unittest.TestCase):
    def setUp(self):
        self.env = Environment.empty()
        self.env.cookbooks.add_cookbook("apache2")

    def tearDown(self):
        pass

    def test_virtual_host_with_server_aliases(self):
        vh = VirtualHost("example.com",
            server_aliases = ["www.example.com"],
            docroot = "/var/www/example.com",
        )

        self.assertEquals(vh.server_name, "example.com")
        self.assertEquals(vh.server_aliases, ["www.example.com"])
        self.assertEquals(vh.docroot, "/var/www/example.com")


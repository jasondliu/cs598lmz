import gc, weakref


class Test_moke_wp_request(BaseTestCase):
	def setUp(self):
		self._init_app()

	def test__moke_wp_request(self):
		obj = moke_wp_request()

		self.assertEqual(obj.method, 'GET')
		self.assertEqual(obj.data, None)
		self.assertIsInstance(obj.headers, CaseInsensitiveDict)

		self.assertEqual(obj.url, 'http://127.0.0.1:80/')
		self.assertEqual(obj.url_scheme, 'http')
		self.assertEqual(obj.url_host, '127.0.0.1:80')
		self.assertEqual(obj.url_hostname, '127.0.0.1')
		self.assertEqual(obj.url_port, 80)
		self.assertEqual(obj.url_path, '/')
		self.assertEqual(obj.url_query_

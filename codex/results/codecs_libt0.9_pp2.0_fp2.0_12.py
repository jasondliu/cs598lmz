import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)



from conf import DB_HOST, DB_USER, DB_PASS


class Connection:

	def __init__(self):
		self._host = DB_HOST
		self._user = DB_USER
		self._password = DB_PASS
		self.connect()


	def connect(self):
		"""Connect to the database and verify the connection."""
		try:
			host = self._host
			user = self._user
			password = self._password
			self.db = MySQLdb.connect(host=host, user=user, passwd=password, use_unicode=True, charset="utf8mb4")
		except Exception as e:
			raise e

	def new_user(self, usr_id, usr, psw):
		"""
		Create an account for a user.
		:param usr: username
		:param p

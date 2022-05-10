import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Test_mikutter_mail_post(unittest.TestCase):
  def setUp(self):
    self.plugin = Plugin.get_by_name('mikutter_mail_post')
    self.plugin.reset_mail_accounts()
    self.account = self.plugin.mail_accounts[0]

    self.user = User('@test')
    self.user.id = 1
    self.user.name = 'test'
    self.user.protected = False
    self.user.created = datetime.datetime.now()

    self.status = Status(self.user, 'test')
    self.status.id = 1
    self.status.text = 'test'
    self.status.created = datetime.datetime.now()

    self.message = self.account.client.fetch(self.account.client.user, '1:1')[0]

  def test_fetch_mail_accounts(self):
    self.assertEqual(len(self.

import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

from src import app, db
from src.models import Note


class NoteModelTestCase(unittest.TestCase):
    """
    This class represents the model test case.
    """

    def setUp(self):
        """
        Define test variables and initialize app.
        """
        self.app = app
        self.db = db

        self.client = self.app.test_client

        self.note = {
            'title': 'Go to Borabora for vacation',
            'description': 'Wishlist'
        }

        # bind the app to current context (for testing purposes)
        with self.app.app_context():
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """
        Remove all records after test is complete.
        """
        with self.app.app_context():
            # drop all tables
            self.db.session.remove()
            self.db

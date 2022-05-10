import select_db
from models.user_model import User
from models.topic_model import Topic

class UserControl():
    def __init__(self, id):
        self.id = id
        self.db = select_db.SelectDB()
        user_str = self.db.user_str(id)
        self.user = User(*user_str)

    def get_topics(self):
        topics_res = self.db.get_topics(self.id)
        topics = []
        for t_res in topics_res:
            topics.append(Topic(*t_res))

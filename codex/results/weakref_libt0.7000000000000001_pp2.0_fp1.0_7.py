import weakref
+
+
+class Session(Base):
+    __tablename__ = 'sessions'
+
+    id = Column(Integer, primary_key=True)
+    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
+    token = Column(String(32), unique=True)
+
+    def __init__(self, user_id, token):
+        self.user_id = user_id
+        self.token = token
+
+    @classmethod
+    def get_session(cls, session_token):
+        session_token = str(session_token)
+        session = DBSession.query(cls).filter_by(token=session_token).one()
+        return session
+
+    @classmethod
+    def create_session(cls, user_id):
+        session_token = uuid.uuid4().hex
+        session = cls(user_id, session_token)
+        DBSession.add(session)
+       

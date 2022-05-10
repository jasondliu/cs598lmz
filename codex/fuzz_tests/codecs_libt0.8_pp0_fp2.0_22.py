import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

db = SQLAlchemy(app)

class User(db.Model):
  __tablename__ = 'survey_user'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), unique=True, nullable=False)
  answers = db.relationship('Answer', backref='survey_user', lazy=False)

  def __repr__(self):
    return '<User %r>' % self.name

class Answer(db.Model):
  __tablename__ = 'survey_answer'
  id = db.Column(db.Integer, primary_key=True)
  value = db.Column(db.Integer, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('survey_user.id'), nullable=False)
  question_id = db.Column(db.Integer, db.ForeignKey

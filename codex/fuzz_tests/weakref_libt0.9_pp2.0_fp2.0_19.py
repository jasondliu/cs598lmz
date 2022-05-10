import weakref
import re
import os

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(64))
    role = db.Column(db.String(16))

    def __init__(self, username, email, password, role='user'):
        self.username = username
        self.email = email
        self.password = hashlib.sha256(password.encode('utf-8'))
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)



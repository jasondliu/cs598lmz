import weakref
from werkzeug.exceptions import NotFound, Forbidden

from app import app, db
from app.models.base import BaseModel, BaseQuery
import app.models.mixins

class User(BaseModel):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    session = db.Column(db.String(255))

    #relations
    owned_groups = db.relationship('Group',
            backref="owner",
            lazy="dynamic",
            cascade="all, delete-orphan")

    #methods
    def set_password(self, password):
        self.password = User.hash_password(password)

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.

from todo import db
from werkzeug.security import generate_password_hash, check_password_hash
from todo import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(user_id=user_id).first()


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)

    @property
    def password():
        raise AttributeError("Password is not a readable attribute.")
    
    @password.setter
    def password(self, entered_password):
        self.password_hash = generate_password_hash(entered_password)

    def verify_password(self, entered_password):
        return check_password_hash(self.password_hash, entered_password)
    
    def get_id(self):
        return (self.user_id)
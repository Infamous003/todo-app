from todo import db

class User(db.Model):
    user_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)

    # @property
    # def password():
    #     raise AttributeError("Password is not a readable attribute.")
    
    # @password.setter
    # def password(self):
    #     pass
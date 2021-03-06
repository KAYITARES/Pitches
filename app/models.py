from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitche',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy="dynamic")
    pass_secure = db.Column(db.String(255))
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitche(db.Model):
    __tablename__= 'pitches' 
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(255))
    category = db.Column(db.String(255))
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'pitche',lazy="dynamic")
  
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_pitches(cls, id):
        pitche = Pitche.query.all()
        return pitche
    
    @classmethod
    def get_category(cls,cat):
        category = Pitch.query.filter_by(category=cat).order_by('-id').all()
        return category

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitches_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    def __repr__(self):
        return f'User {self.comment}'

@classmethod
def get_pitches(cls):
    pitches = Pitche.query.filter_by().all()
    return pitches
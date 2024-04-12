from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class FOOD(db.Model):
    __tablename__ = 'foods'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date, nullable=False)
    memo = db.Column(db.Text)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', name="fk_foods_users"), nullable=False)
    user = relationship("User", back_populates = "foods")
    
class FOOD_NEEDED(db.Model):
    __tablename__ = 'foods_needed'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    memo = db.Column(db.Text)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', name="fk_foods_needed"), nullable=False)
    user = relationship("User", back_populates = "foods_needed")
    
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    foods = relationship("FOOD", back_populates = "user")
    foods_needed = relationship("FOOD_NEEDED", back_populates="user")
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password_hash(self, password):
        return check_password_hash(self.password, password)
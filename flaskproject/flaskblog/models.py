from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin  # Class which provides the basic parameters to validate user login 


@login_manager.user_loader		# Required for flask-login extension to load user from user_id stored in session
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique = True, nullable = False)
	email = db.Column(db.String(120), unique = True, nullable = False)
	image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
	password = db.Column(db.String(20), nullable = False)
	#authenticated = db.Column(db.Boolean, default=False)
	posts = db.relationship('Post', backref = 'author', lazy = True) #Here 'Post' is the actual classname/tablename

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100), nullable = False)
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.Text, nullable = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) #Here 'user.id' represents 'id' 
																				#column of table named 'user'
																				#(Automatically converted to lower 
																				#case by 'User' class)
	def __repr__(self):
		return f"User('{self.title}', '{self.date_posted}')"
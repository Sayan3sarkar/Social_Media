import os

class Config:

	SECRET_KEY = 'how_you_doin'
	db_path = os.path.join(os.path.dirname(__file__), 'site.db')# __file__ gives the pathname of the file from which the module(flaskblog.py) in this case was loaded
	db_uri = f'sqlite:///{db_path}' #db_uri = 'sqlite:///{}'.format(db_path)(Same as above use this if python version < 3.6)
	SQLALCHEMY_DATABASE_URI = db_uri
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = 'gvlhxicletbhxhts'#You have to enable 2 step verification in your google account and then create an app password for application named 'app'. You have to use that instead of the *** mentioned in the password
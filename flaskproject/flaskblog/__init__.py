from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'how_you_doin'

db_path = os.path.join(os.path.dirname(__file__), 'site.db')# __file__ gives the pathname of the file from which the module(flaskblog.py) in this case was loaded
db_uri = f'sqlite:///{db_path}' #db_uri = 'sqlite:///{}'.format(db_path)(Same as above use this if python version < 3.6)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #Fucntion name of route /login
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = '****'#You have to enable 2 step verification in your google account and then create an app password for application named 'app'. You have to use that instead of the *** mentioned in the password

mail = Mail(app)

from flaskblog import routes
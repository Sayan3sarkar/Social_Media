import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


#Saving user profile picture method
def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

	#Resizing uploaded image to 125x125
	output_size = (125,125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)

	i.save(picture_path)
	return picture_fn


#Sending password reset token to user
def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request', sender='saya3n.sarkar@gmail.com', recipients=[user.email])
	msg.body = f''' To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

Note: This link is active only for 5 minutes

If you did'nt make this request, ignore this mail.
'''
	mail.send(msg)
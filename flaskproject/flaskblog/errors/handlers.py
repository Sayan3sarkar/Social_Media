from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
	return render_template('errors/404.html'), 404 #Second return argument is status code which is 200 by default. So we
												   # did'nt mention it in routes but for errors we have to specify

@errors.app_errorhandler(403)
def error_403(error):
	return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
	return render_template('errors/500.html'), 500